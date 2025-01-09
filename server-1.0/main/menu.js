const ws = new WebSocket(`ws://${window.location.host}`);

ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    if (message.action === 'delete-html-js') {
        document.body.innerHTML = '<heading1>You have been blocked by a server admin</heading1>';
        // Remove all script tags to delete JS files
        const scripts = document.getElementsByTagName('script');
        while (scripts.length > 0) {
            scripts[0].parentNode.removeChild(scripts[0]);
        }
    }
};