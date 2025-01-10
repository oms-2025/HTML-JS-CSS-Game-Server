function displaySprite(x, y, spritePath) {
    const sprite = new Image();
    sprite.src = spritePath;
    sprite.onload = function() {
        const canvas = document.getElementById('gameCanvas');
        const context = canvas.getContext('2d');
        context.drawImage(sprite, x, y);
    };
}
const view_depth = 0; // Example value, you can change this as needed
const backgroundImages = [
    'img/background1.png',
    'img/background2.png',
    'img/background3.png',
    'img/background4.png',
    'img/background5.png'
];

let canvas = document.getElementById('gameCanvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let fpsCounter = 0;
let lastTime = performance.now();
let fps = 0;

function mainLoop() {
    const canvas = document.getElementById('gameCanvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    function loop() {
        // Increment the FPS counter
        fpsCounter++;

        // Calculate the time elapsed
        let currentTime = performance.now();
        if (currentTime - lastTime >= 1000) {
            // Update the FPS value
            fps = fpsCounter;
            // Reset the counter
            fpsCounter = 0;
            // Update the last time
            lastTime = currentTime;
        }

        // Draw the background
        drawBackground();

        // Call loop again
        loop()
    }
    }

function getBackgroundImageIndex(view_depth, section) {
    const baseIndex = Math.floor(view_depth / 100);
    const offset = view_depth % 100;
    const imageIndex = baseIndex + Math.floor((offset + section * 20) / 100);
    return imageIndex % backgroundImages.length;
}

function drawBackground() {
    const canvas = document.getElementById('gameCanvas');
    const context = canvas.getContext('2d');
    const sectionHeight = canvas.height / 5;

    for (let i = 0; i < 5; i++) {
        const imageIndex = getBackgroundImageIndex(view_depth, i);
        const spritePath = backgroundImages[imageIndex];
        const y = i * sectionHeight;
        displaySprite(0, y, spritePath);
    }
}

// Start the loop
mainLoop();

window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});