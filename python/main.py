import os
from club import clubs
from sim import *
from fixture import *

def menu():
    os.system('cls')
    v = ''
    while v not in ['1', '2', '3', '4']:
        print('\n+------+')
        print('| MENU |')
        print('+------+\n')
        print('1 > Table')
        print('2 > Upcoming fixtures')
        print('3 > Results')
        print('4 > EXIT')    
        
        v = input('\nGO TO >>> ')
        
    match v:
        case '1':
            table()
        case '2':
            upcoming_fixtures()
        case '3':
            prev_results()
        case '4':
            os.system('exit')

def table():
    os.system('cls')
    print('\n+-------+')
    print('| TABLE |')
    print('+-------+\n')
    print('  CLUB  |    POINTS     |  PLAYED GAMES')
    print('--------|---------------|----------------')
    for c in clubs:
        print(f'{c.abbr}\t|\t{points[c.abbr]}\t|\t{played_games[c.abbr]}')
    print('-----------------------------------------')
    input('\nMENU >>> ')
    menu()

def prev_results():
    pass

def upcoming_fixtures():
    i = 0
    for f in fixtures:
        print(i)
        print(f'{f.home.name} - {f.away.name}')
        i+=1

    os.system('cls')
    print('\n+-------------------+')
    print('| UPCOMING FIXTURES |')
    print('+-------------------+\n')
    v=0
    while v not in range(1, 100):
        v = int(input(f'Enter round number 1-{number_of_rounds}: '))
    nem jó ez itt
    print(f'\nROUND {v} FIXTURES:\n')
    for f in fixtures[ ( (v-1) *  int(len(clubs)/2) ) : (v * int(len(clubs)/2) )]:
        print(f'{f.home.name} - {f.away.name}')
        print(f'{f.home_odds} | {f.draw_odds} | {f.away_odds}')
        print()
        





reset()

round_robin()

menu()
                                                               






























# for f in fixtures[0:10]:
#     print(f'{f.home.name} - {f.away.name}')




 
'''
    
for i in range(0, len(fixtures)):
    print(f'{fixtures[i].home.name}   -   {fixtures[i].away.name}')
    print(f'{fixtures[i].home_odds}  -  {fixtures[i].draw_odds}  -  {fixtures[i].away_odds}')
    print()

input(f'\nFORDULÓ SZIMULÁLÁSA >>>')
print('\n')

for i in range(0, len(fixtures)):
        print(f'{fixtures[i].home.name}   -   {fixtures[i].away.name}')
        match fixtures[i].simulating_result(i):
            case 'H':
                print(f'Győztes: {fixtures[i].home.name} ({fixtures[i].home_odds})')
            case 'D':
                print(f'Döntetlen ({fixtures[i].draw_odds})')
            case 'A':
                print(f'Győztes: {fixtures[i].away.name} ({fixtures[i].away_odds})')
        print()




print(points)

'''










