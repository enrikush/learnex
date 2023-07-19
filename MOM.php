<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
    <title>User Dashboard</title>
    <style>
        body {
            font-family: Verdana, Arial, sans-serif;
        }

        /* CSS for transitions */
        .transition {
            opacity: 0;
            transition: opacity 0.5s;
        }

        .visible {
            opacity: 1;
        }

        button {
            transform: translatex(-119px) translatey(-50px);
            position: relative;
            left: 400px;
            top: 178px;
            bottom: 367px;
            right: 400px;
            z-index: 0;
            width: 262px;
            min-height: 391px;
            background-color: #ffffff;
            backdrop-filter: brightness(0) contrast(0) grayscale(1) saturate(0);
            background-repeat: repeat-x;
            background-clip: padding-box;
            border-width: 1px;
            border-top-left-radius: 50px;
            border-top-right-radius: 50px;
            border-bottom-left-radius: 50px;
            border-bottom-right-radius: 50px;
            font-family: Verdana, Geneva, sans-serif;
            text-transform: none;
            box-shadow: 0px 0px 25px 0px #5d5959;
            height: 442px;
            min-width: 283px;
            padding-left: 0px;
            margin-left: 50px;
        }

        /* Login header */
        #login-header {
            transform: translatex(641px) translatey(18px);
            width: 21% !important;
        }

        /* CSS for main buttons */
        .main-button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin: 10px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .main-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
<h1 id="login-header">Logged in as <span><?php echo isset($_SESSION['nickname']) ? $_SESSION['nickname'] : ''; ?></span></h1>
<div id="button">
    <button onclick="event.preventDefault(); location.href='file1.html'">file1</button>
    <button onclick="event.preventDefault(); location.href='file2.html'">file2</button>
    <button onclick="event.preventDefault(); location.href='file3.html'">file3</button>
</div>
<div id="fileContainer"></div>
</body>
</html>
