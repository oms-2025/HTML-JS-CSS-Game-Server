const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const fs = require('fs');
const { exec } = require('child_process');
const WebSocket = require('ws');

const app = express();
const port = 3000;
let serverProcess = null;
let ipAddresses = [];
let blockedIps = [];
const clients = new Map();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Serve the server control interface
app.get('/server-control', (req, res) => {
    res.sendFile(path.join(__dirname, 'server.html'));
});

// Serve the menu HTML file to the end user
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'menu.html'));
});

// Dynamic static file serving
app.use('/main/:game', (req, res, next) => {
    const game = req.params.game;
    const gamePath = path.join(__dirname, 'main', game);
    express.static(gamePath)(req, res, next);
});

// Load user credentials from a file (for simplicity, using a JSON file)
const users = JSON.parse(fs.readFileSync('endusers.json', 'utf8'));

// Load admin credentials from a file
const admins = JSON.parse(fs.readFileSync('admin.json', 'utf8'));

// Login endpoint for end users
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(user => user.username === username);
    if (user && user.password === password) {
        res.json({ success: true });
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
        serverProcess = exec('node server.js', (error, stdout, stderr) => {
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

// Get IP addresses
app.get('/ip-addresses', (req, res) => {
    res.json(ipAddresses);
});

// Get current user's IP address
app.get('/current-ip', (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    res.json({ ip });
});

// Block IP addresses
app.post('/block-ips', (req, res) => {
    blockedIps = [...new Set([...blockedIps, ...req.body.ips])];

    // Send a message to all blocked IPs to delete the HTML and JS files
    blockedIps.forEach(ip => {
        const client = clients.get(ip);
        if (client) {
            client.send(JSON.stringify({ action: 'delete-html-js' }));
        }
    });

    res.send('IP addresses blocked');
});

// Unblock IP addresses
app.post('/unblock-ips', (req, res) => {
    blockedIps = blockedIps.filter(ip => !req.body.ips.includes(ip));
    res.send('IP addresses unblocked');
});

// Create HTTP server
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
    });
});

// Client-side JavaScript for handling button clicks
app.get('/server/main/server.js', (req, res) => {
    res.type('.js');
    res.send(`
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('startServer').addEventListener('click', function() {
                fetch('/start-server', {
                    method: 'POST'
                })
                .then(response => response.text())
                .then(data => alert(data))
                .catch(error => console.error('Error:', error));
            });

            document.getElementById('stopServer').addEventListener('click', function() {
                fetch('/stop-server', {
                    method: 'POST'
                })
                .then(response => response.text())
                .then(data => alert(data))
                .catch(error => console.error('Error:', error));
            });

            document.getElementById('blockIpButton').addEventListener('click', function() {
                const blockIpMenu = document.getElementById('blockIpMenu');
                blockIpMenu.style.display = blockIpMenu.style.display === 'none' ? 'block' : 'none';
            });

            document.getElementById('blockIp').addEventListener('click', function() {
                const ipAddress = document.getElementById('ipAddress').value;
                fetch('/block-ips', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ ips: [ipAddress] })
                })
                .then(response => response.text())
                .then(data => alert(data))
                .catch(error => console.error('Error:', error));
            });

            document.getElementById('unblockIp').addEventListener('click', function() {
                const ipAddress = document.getElementById('ipAddress').value;
                fetch('/unblock-ips', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ ips: [ipAddress] })
                })
                .then(response => response.text())
                .then(data => alert(data))
                .catch(error => console.error('Error:', error));
            });
        });
    `);
});