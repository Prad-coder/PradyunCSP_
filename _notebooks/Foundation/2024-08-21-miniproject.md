---
layout: post
title: Mini Project
description:  A Gaming Blog!
type: issues
comments: true
permalink: /miniproject/home
menu: nav/miniproject.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gaming Blog</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <header>
        <div class="container">
            <h1>Gaming Blog</h1>
            <nav id="submenu">
                <ul>
                    <li><a href="#games">Games</a></li>
                    <li><a href="#tips">Tips & Tricks</a></li>
                    <li><a href="#mods">Mods</a></li>
                    <li><a href="#community">Community</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <section id="games">
            <div class="container">
                <h2>Games</h2>
                <p>Minecraft: A block game with RNG generation of worlds in which players have to survive and beat the final boss, The Ender Dragon. Fortnite: A third-person shooter game in which players fight to be the last one standing. Roblox: An online gaming platform in which there are different user-made games where people can play. Brawl Stars: A 3v3 multiplayer and battle royale game in which players brawl for different goals to gain trophies. Valorant: A first person shooter game in which players fight against other players and gain ranks.</p>
            </div>
        </section>
        <section id="tips">
            <div class="container">
                <h2>Tips & Tricks</h2>
                <p>Enhance your gaming skills with these useful tips and tricks. Whether you're a novice or a pro, you'll find valuable advice to improve your gameplay.</p>
                <button id="randomTipButton">Get Random Tip</button>
                <p id="randomTip"></p>
            </div>
        </section>
        <section id="mods">
            <div class="container">
                <h2>Mods</h2>
                <p>Explore popular mods that can enhance and customize your gaming experience. Find mods for a variety of games and take your gameplay to the next level.</p>
            </div>
        </section>
        <section id="community">
            <div class="container">
                <h2>Community</h2>
                <p>Join the conversation with other gamers. Check out forums, social media groups, and other community resources to connect with fellow enthusiasts.</p>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2024 Gaming Blog. All rights reserved.</p>
        </div>
    </footer>
    <script src="miniproject.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
