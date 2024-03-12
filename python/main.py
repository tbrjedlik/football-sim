import os
from club import clubs
from sim import *
from fixture import *


reset()

print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')

round_robin()








for f in fixtures[0:10]:
    print(f'{f.home.name} - {f.away.name}')




 
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










