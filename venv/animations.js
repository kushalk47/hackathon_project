document.addEventListener("DOMContentLoaded", function () {
    let body = document.body;
    body.style.overflow = "hidden";
    let canvas = document.createElement("canvas");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    document.body.appendChild(canvas);
    let ctx = canvas.getContext("2d");
    let matrix = "abcdefghijklmnopqrstuvwxyz0123456789".split("");
    let font_size = 10;
    let columns = canvas.width / font_size;
    let drops = [];
    for (let x = 0; x < columns; x++) drops[x] = 1;
    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "#00ffcc";
        ctx.font = font_size + "px Courier";
        for (let i = 0; i < drops.length; i++) {
            let text = matrix[Math.floor(Math.random() * matrix.length)];
            ctx.fillText(text, i * font_size, drops[i] * font_size);
            if (drops[i] * font_size > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 33);
});
