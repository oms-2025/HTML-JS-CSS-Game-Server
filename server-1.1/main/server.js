const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const fs = require('fs');
const { exec } = require('child_process');
const WebSocket = require('ws');

const app = express();
let port = 3000; // Make port variable to allow changes
let serverProcess = null;
let ipAddresses = [];
let blockedIps = [];
const clients = new Map();
const activeUsers = new Map(); // Map to store active users and their IP addresses

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Serve the server control interface
app.get('/server-control', (req, res) => {
    res.sendFile(path.join(__dirname, 'server-1.1/main/server.html'));
});

// Serve the menu HTML file to the end user
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'server-1.1/main/menu.html'));
});

// Dynamic static file serving
app.use('/main/:game', (req, res, next) => {
    const game = req.params.game;
    const gamePath = path.join(__dirname, 'main', game);
    express.static(gamePath)(req, res, next);
});

// Load user credentials from a file (for simplicity, using a JSON file)
const users = JSON.parse(fs.readFileSync('server-1.1/main/endusers.json', 'utf8'));

// Load admin credentials from a file
const admins = JSON.parse(fs.readFileSync('server-1.1/main/admin.json', 'utf8'));

// Login endpoint for end users
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(user => user.username === username);
    if (user && user.password === password) {
        if (activeUsers.has(username)) {
            res.send('<html><body><h1>This username is already in use.</h1></body></html>');
        } else {
            const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
            activeUsers.set(username, ip);
            res.json({ success: true });
        }
    } else {
        res.json({ success: false });
    }
});

// Login endpoint for admins
app.post('/admin-login', (req, res) => {
    const { username, password } = req.body;
    const admin = admins.find(admin => admin.username === username);
    if (admin && bcrypt.compareSync(password, admin.password)) {
        res.json({ success: true });
    } else {
        res.json({ success: false });
    }
});

// Start the server
app.post('/start-server', (req, res) => {
    if (!serverProcess) {
        serverProcess = exec('node server-1.1/main/server.js', (error, stdout, stderr) => {
            if (error) {
                console.error(`exec error: ${error}`);
                return;
            }
            console.log(`stdout: ${stdout}`);
            console.error(`stderr: ${stderr}`);
        });
        res.send('Server started');
    } else {
        res.send('Server is already running');
    }
});

// Stop the server
app.post('/stop-server', (req, res) => {
    if (serverProcess) {
        serverProcess.kill();
        serverProcess = null;
        res.send('Server stopped');
    } else {
        res.send('Server is not running');
    }
});

// Change server port
app.post('/change-port', (req, res) => {
    const newPort = parseInt(req.body.newPort, 10);
    if (isNaN(newPort) || newPort <= 0 || newPort > 65535) {
        return res.status(400).send('Invalid port number');
    }

    // Send redirect message to all clients
    clients.forEach((client, ip) => {
        client.send(JSON.stringify({ action: 'redirect', newPort }));
    });

    // Stop the current server
    if (serverProcess) {
        serverProcess.kill();
        serverProcess = null;
    }

    // Update the port and restart the server
    port = newPort;
    startServer();

    res.send(`Server port changed to ${newPort}`);
});

// Log IP addresses
app.use((req, res, next) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    if (!ipAddresses.includes(ip)) {
        ipAddresses.push(ip);
    }
    if (blockedIps.includes(ip)) {
        res.status(403).send('Access denied');
    } else {
        next();
    }
});

// Get IP addresses and associated usernames
app.get('/ip-addresses', (req, res) => {
    const ipUsernames = Array.from(activeUsers.entries()).map(([username, ip]) => ({ ip, username }));
    res.json(ipUsernames);
});

// Get current user's IP address
app.get('/current-ip', (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    res.json({ ip });
});

// Block IP addresses
app.post('/block-ips', (req, res) => {
    const adminUsername = req.body.adminUsername;
    blockedIps = [...new Set([...blockedIps, ...req.body.ips])];

    // Send a message to all blocked IPs to delete the HTML and JS files
    blockedIps.forEach(ip => {
        const client = clients.get(ip);
        if (client) {
            client.send(JSON.stringify({ action: 'delete-html-js', admin: adminUsername }));
        }
    });

    res.send('IP addresses blocked');
});

// Unblock IP addresses
app.post('/unblock-ips', (req, res) => {
    blockedIps = blockedIps.filter(ip => !req.body.ips.includes(ip));
    res.send('IP addresses unblocked');
});

// Function to start the server
const startServer = async () => {
    try {
        const { publicIpv4 } = await import('public-ip');
        const publicIp = await publicIpv4();
        const server = app.listen(port, '0.0.0.0', () => {
            console.log(`Server control interface is running at http://${publicIp}:${port}/server-control`);
        });

        // Create WebSocket server
        const wss = new WebSocket.Server({ server });

        wss.on('connection', (ws, req) => {
            const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
            clients.set(ip, ws);

            ws.on('close', () => {
                clients.delete(ip);
                // Remove the user from activeUsers map when they disconnect
                for (const [username, userIp] of activeUsers.entries()) {
                    if (userIp === ip) {
                        activeUsers.delete(username);
                        break;
                    }
                }
            });
        });
    } catch (err) {
        console.error('Failed to get public IP address:', err);
        const server = app.listen(port, '0.0.0.0', () => {
            console.log(`Server control interface is running at http://0.0.0.0:${port}/server-control`);
        });

        // Create WebSocket server
        const wss = new WebSocket.Server({ server });

        wss.on('connection', (ws, req) => {
            const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
            clients.set(ip, ws);

            ws.on('close', () => {
                clients.delete(ip);
                // Remove the user from activeUsers map when they disconnect
                for (const [username, userIp] of activeUsers.entries()) {
                    if (userIp === ip) {
                        activeUsers.delete(username);
                        break;
                    }
                }
            });
        });
    }
};

// Start the server initially
startServer();