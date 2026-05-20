<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Klasik Yılan Oyunu</title>
    <style>
        body {
            background-color: #111;
            color: white;
            font-family: 'Poppins', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        h1 {
            margin-bottom: 10px;
            font-size: 24px;
        }
        #score-board {
            font-size: 20px;
            margin-bottom: 15px;
            font-weight: bold;
            color: #4CAF50;
        }
        canvas {
            border: 4px solid #fff;
            background-color: #222;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }
        .controls {
            margin-top: 15px;
            font-size: 14px;
            color: #888;
        }
    </style>
</head>
<body>

    <h1>YILAN OYUNU</h1>
    <div id="score-board">Skor: <span id="score">0</span></div>
    <canvas id="gameCanvas" width="400" height="400"></canvas>
    <div class="controls">Oynamak için yön (ok) tuşlarını kullanın.</div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const scoreElement = document.getElementById("score");

        const gridSize = 20;
        const tileCount = canvas.width / gridSize;

        let snake = [{ x: 10, y: 10 }];
        let food = { x: 5, y: 5 };
        let dx = 1;
        let dy = 0;
        let score = 0;
        let gameSpeed = 100; // Milisaniye cinsinden hız (Düşük sayı = Daha hızlı)
        let gameLoop;

        function main() {
            if (hasGameEnded()) {
                alert("Oyun Bitti! Toplam Skorun: " + score);
                resetGame();
            }

            clearCanvas();
            drawFood();
            moveSnake();
            drawSnake();
        }

        // Oyunu başlat
        resetGame();

        function clearCanvas() {
            ctx.fillStyle = "#222";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        function drawSnake() {
            ctx.fillStyle = "#4CAF50"; // Yılanın rengi yeşil
            snake.forEach((part, index) => {
                // Kafası biraz daha koyu yeşil olsun
                if (index === 0) ctx.fillStyle = "#388E3C";
                else ctx.fillStyle = "#4CAF50";
                
                ctx.fillRect(part.x * gridSize, part.y * gridSize, gridSize - 2, gridSize - 2);
            });
        }

        function moveSnake() {
            const head = { x: snake[0].x + dx, y: snake[0].y + dy };
            snake.unshift(head);

            // Yılan yemi yedi mi?
            if (snake[0].x === food.x && snake[0].y === food.y) {
                score += 10;
                scoreElement.innerText = score;
                generateFood();
            } else {
                snake.pop(); // Yem yemediyse kuyruğu sil (ilerleme hissi)
            }
        }

        function drawFood() {
            ctx.fillStyle = "#FF5722"; // Yemin rengi kırmızı
            ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
        }

        function generateFood() {
            food.x = Math.floor(Math.random() * tileCount);
            food.y = Math.floor(Math.random() * tileCount);

            // Yem yılanın üstünde çıkmasın
            snake.forEach(part => {
                if (part.x === food.x && part.y === food.y) {
                    generateFood();
                }
            });
        }

        function hasGameEnded() {
            // Duvara çarpma kontrolü
            if (snake[0].x < 0 || snake[0].x >= tileCount || snake[0].y < 0 || snake[0].y >= tileCount) {
                return true;
            }
            // Kendi kuyruğuna çarpma kontrolü
            for (let i = 1; i < snake.length; i++) {
                if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) {
                    return true;
                }
            }
            return false;
        }

        function resetGame() {
            clearInterval(gameLoop);
            snake = [{ x: 10, y: 10 }];
            food = { x: 5, y: 5 };
            dx = 1;
            dy = 0;
            score = 0;
            scoreElement.innerText = score;
            generateFood();
            gameLoop = setInterval(main, gameSpeed);
        }

        // Klavye Kontrolleri
        document.addEventListener("keydown", changeDirection);

        function changeDirection(event) {
            const keyPressed = event.keyCode;
            const LEFT = 37;
            const UP = 38;
            const RIGHT = 39;
            const DOWN = 40;

            const goingUp = dy === -1;
            const goingDown = dy === 1;
            const goingRight = dx === 1;
            const goingLeft = dx === -1;

            if (keyPressed === LEFT && !goingRight) {
                dx = -1;
                dy = 0;
            }
            if (keyPressed === UP && !goingDown) {
                dx = 0;
                dy = -1;
            }
            if (keyPressed === RIGHT && !goingLeft) {
                dx = 1;
                dy = 0;
            }
            if (keyPressed === DOWN && !goingUp) {
                dx = 0;
                dy = 1;
            }
        }
    </script>
</body>
</html
