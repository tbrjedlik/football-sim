from club import clubs
import os
from time import sleep

def prob_to_odd(prob:float) -> float:
    odd = 1 / prob
    return odd

points = dict()
played_games = dict()
for c in clubs:
    points[c.abbr] = 0
    played_games[c.abbr] = 0

def reset():
    os.system('cls')
    
    if not os.path.exists('results'):
        os.makedirs('results')
    
    f = open('results/results.txt', 'w', encoding='utf-8')
    f.write('')
    f.close()
    
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="dist/bootstrap.min.css">
        <link rel="stylesheet" href="styles.css">
        <title>Teams</title>
    </head>
    <body>
    <header>
        <nav class="navbar navbar-expand-lg" data-bs-theme="dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="index.html"><img class="indexlogo" src="pictures/logo.png" alt=""></a>
            <button class="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="navbar-collapse collapse textb" id="navbarNavAltMarkup" style="">
            <div class="navbar-nav">
                <a class="nav-link textb" href="teams.html">Teams</a>
                <a class="nav-link textb" href="theleague.html">The League</a>
                <a class="nav-link textb" href="creators.html">Creators</a>
            </div>
            </div>
        </div>
        </nav>
    </header>
    <header>
        <div class="side-line left"></div>
        <div class="side-line right"></div>
    </header>
    <div class="containers">
        <h1 class="title">The League</h1>
        <p class="text-center mt-5 creator-text">Download the project <a href="https://github.com/tbrjedlik/football-sim">HERE</a> and come back after simulating.</p>
    </div>
    </body>
    </html>
    '''
    
    f = open('web/theleague.html', 'w', encoding='utf-8')
    f.write(html_content)
    f.close()
    
def main_title():
    os.system('cls')
    
    print()
    print()
    print('   ________  ____  _________  ___   __   __     __________  ___')
    print('  / __/ __ \/ __ \/_  __/ _ )/ _ | / /  / /    / __/  _/  |/  /')
    print(' / _// /_/ / /_/ / / / / _  / __ |/ /__/ /__  _\ \_/ // /|_/ / ')
    print('/_/  \____/\____/ /_/ /____/_/ |_/____/____/ /___/___/_/  /_/  ')
    print()
    print()

    sleep(0.5)
    
    input('CONTINUE >>> ')
    
    os.system('cls')