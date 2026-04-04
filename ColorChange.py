<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<style>
  body {
    transition: background-color 0.3s ease;
  }
  .hidden {
    display: none;
  }
</style>
<body>
    <div class="hidden">r=1, g=2, b=3</div>

    <script>
      function runLoop() {
        setTimeout(() => { document.body.style.backgroundColor = "green"; }, 0);
        setTimeout(() => { document.body.style.backgroundColor = "red"; },   1000);
        setTimeout(() => { document.body.style.backgroundColor = "blue"; },  2000);
        setTimeout(() => { document.body.style.backgroundColor = "green"; }, 3000);
        setTimeout(() => { document.body.style.backgroundColor = "blue"; },  4000);
        setTimeout(() => { document.body.style.backgroundColor = "red"; },   5000);
        setTimeout(() => { document.body.style.backgroundColor = ""; runLoop(); }, 11000);
      }

      runLoop();
    </script>
</body>
</html>
