import os, subprocess
from club import clubs
from sim import *
from standing import *
from fixture import *
upcoming_round = 1
sorted_by_points = sorted(points.items(), key=lambda x: x[1], reverse=True)

def the_league_writing():
    f = open('web/theleague.html', 'w', encoding='utf-8')
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
    </div>
    <div class="card centered mt-5 mb-5" style="width: 30rem;">
        <div class="card-header standing-text">
            Standings
        </div>
        <ul class="list-group list-group-flush">
          
    '''
    f.write(html_content)


    
    i=1
    for s in standings:
        f.write(f'<li class="list-group-item">{i} | {s.abbr} ({s.points})</li>\n')
        i+=1
    html_content = '''
            </ul>
      </div>
    </body>
    </html>
    '''
    f.write(html_content)
    f.close()
    

def menu():
    global upcoming_round

    v = ''
    while v not in ['1', '2', '3', '4', '5']:
        os.system('cls')
        print('\n+------+')
        print('| MENU |')
        print('+------+\n')
        
        if upcoming_round < 39:
            print(f'Upcoming round: {upcoming_round}\n')
        
            print('1 > Table')
            print('2 > Upcoming fixtures')
            print('3 > Results')
            print('4 > Simulating')
            print('5 > EXIT')
            
            v = input('\nGO TO >>> ')
            
            match v:
                case '1':
                    table()
                case '2':
                    upcoming_fixtures()
                case '3':
                    prev_results()
                case '4':
                    simulating()
                case '5':
                    y_n = ''
                    while y_n not in ['y','n']:
                        print('')
                        y_n = input(f'Are you sure you want to exit? (y/n): ')
                    if y_n.lower() == 'y':
                        os.system('exit')
                    else:
                        menu()
                
        else:
            
            while v not in ['1', '2', '3', '4']:
                os.system('cls')
                print('\n+------+')
                print('| MENU |')
                print('+------+\n')
            
                print(f'The season is over.\n')
            
                print('1 > Table')
                print('2 > Results')
                print('3 > NEW SIMULATION')
                print('4 > EXIT')
                
                v = input('\nGO TO >>> ')
                
                match v:
                    case '1':
                        table()
                    case '2':
                        prev_results()
                    
                    case '3':
                        y_n = ''
                        print('')
                        while y_n not in ['y','n']:
                            y_n = input(f'Are you want to start a new simulation? (y/n): ')
                        if y_n.lower() == 'y':
                            subprocess.run(["python", "python/main.py"])
                            os.system('exit')
                        else:
                            menu()
                        
                    case '4':
                        y_n = ''
                        while y_n not in ['y','n']:
                            y_n = input(f'Are you sure you want to exit? (y/n): ')
                        if y_n.lower() == 'y':
                            os.system('exit')
                        else:
                            menu()

def table():
    global sorted_by_points
    
    os.system('cls')
    print('\n+-------+')
    print('| TABLE |')
    print('+-------+\n')
    print('  CLUB  |    POINTS     |  PLAYED GAMES')
    print('--------|---------------|----------------')
    sorted_by_points = sorted(points.items(), key=lambda x: x[1], reverse=True)

    f = open('results/standings.csv', 'w', encoding='utf-8')

    for k, v in sorted_by_points:
        print(f'{k}\t|\t{v}\t|\t{played_games[k]}')
        f.write(f'{k};{v}\n')
        
    f.close()
    
    the_league_writing()

    
    
        

    print('-----------------------------------------')
    input('\nMENU >>> ')
    menu()
    

            
    
    
        
    

def prev_results():
    global upcoming_round

    if upcoming_round == 1:
        os.system('cls')
        print('\n+---------+')
        print('| RESULTS |')
        print('+---------+\n')
        print('No results yet.')
        input('\nMENU >>> ')
        menu()
        
    os.system('cls')
    print('\n+---------+')
    print('| RESULTS |')
    print('+---------+\n')
    
    v = 0
    
    while v not in range(1, upcoming_round):

        user_input = input(f'Enter round number ({1}-{upcoming_round-1}) or type "M" for menu: ')
        if user_input.lower() == "m":
            menu()
            break
        elif user_input.isdigit():
            v = int(user_input)
        if v in range(1, upcoming_round):

            os.system('cls')
            print('\n+---------+')
            print('| RESULTS |')
            print('+---------+\n')

            print(f'\nROUND {v} RESULTS:\n')

            for f in fixtures[ ( (v-1) *  int(len(clubs)/2) ) : (v * int(len(clubs)/2) )]:
                print(f'{f.home.name} {f.home_score} - {f.away_score} {f.away.name}')
                print()
            
            v = 0

def upcoming_fixtures():
    global upcoming_round

    os.system('cls')
    print('\n+-------------------+')
    print('| UPCOMING FIXTURES |')
    print('+-------------------+\n')
    
    v = 0
    
    while v not in range((upcoming_round), number_of_rounds + 1):

        user_input = input(f'Enter round number ({upcoming_round}-{number_of_rounds}) or type "M" for menu: ')
        if user_input.lower() == "m":
            menu()
            break
        elif user_input.isdigit():
            v = int(user_input)
        if v in range(upcoming_round, number_of_rounds + 1):

            os.system('cls')
            print('\n+-------------------+')
            print('| UPCOMING FIXTURES |')
            print('+-------------------+\n')

            print(f'\nROUND {v} FIXTURES:\n')

            for f in fixtures[ ( (v-1) *  int(len(clubs)/2) ) : (v * int(len(clubs)/2) )]:
                print(f'{f.home.name} - {f.away.name}')
                print(f'{f.home_odds} | {f.draw_odds} | {f.away_odds}')
                print()
            
            v = 0

def simulating():
    global upcoming_round
    os.system('cls')
    print('\n+------------+')
    print('| SIMULATING |')
    print('+------------+\n')
    
    v = 0
    
    while ( v not in range(1, number_of_rounds + 1) ) or ( v < upcoming_round ):

        user_input = input(f'Enter round number ({upcoming_round}-{number_of_rounds}) you want to simulate or type "M" for menu: ')
        if user_input.lower() == "m":
            menu()
            break
        elif user_input.isdigit():
            v = int(user_input)
        if v in range(upcoming_round, number_of_rounds + 1):

            os.system('cls')
            print('\n+------------+')
            print('| SIMULATING |')
            print('+------------+\n')

            if v != upcoming_round:
                y_n = ''
                while y_n not in ['y','n']:
                    y_n = input(f'The next round is not round {v}. Do you want to skip to round {v}? (y/n): ')
                    if y_n.lower() == 'y':
                        pass
                    else:
                        simulating()
                        
            print('\nThese fixtures will be simulated:\n')

            for f in fixtures[(upcoming_round-1) * int(len(clubs)/2) : (v * int(len(clubs)/2) )]:
                print(f'{f.home.name} - {f.away.name}')
                print(f'{f.home_odds} | {f.draw_odds} | {f.away_odds}')
                print()
                        
            y_n = ''
            while y_n not in ['y','n']:
                y_n = input(f'Do you want to simulate these fixtures? (y/n): ')
                if y_n.lower() == 'y':
                    for f in fixtures[(upcoming_round-1) * int(len(clubs)/2) : (v * int(len(clubs)/2) )]:
                        f.simulating_result()
                        
                    os.system('cls')
                    print('\n+------------+')
                    print('| SIMULATING |')
                    print('+------------+\n')
                    print(f'{(v * int(len(clubs)/2) )} fixtures have been simulated.')
                    upcoming_round = v + 1

                    input('\nMENU >>> ')
                    menu()
                        
                else:
                    input('\nMENU >>> ')
                    menu()


reset()

main_title()

round_robin()
fixtures = matches + rematches

menu()