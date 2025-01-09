document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('loginScreen').style.display = 'none';
            document.getElementById('gameMenu').style.display = 'block';
        } else {
            document.getElementById('loginError').textContent = 'Invalid credentials or username already in use.';
        }
    })
    .catch(error => console.error('Error:', error));
});

const ws = new WebSocket(`ws://${window.location.host}`);

ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    if (message.action === 'delete-html-js') {
        document.body.innerHTML = '<h1>You have been blocked by a server admin</h1>';
        // Remove all script tags to delete JS files
        const scripts = document.getElementsByTagName('script');
        while (scripts.length > 0) {
            scripts[0].parentNode.removeChild(scripts[0]);
        }
    }
};