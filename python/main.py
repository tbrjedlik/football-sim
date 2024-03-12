import os
from club import clubs
from sim import *
from fixture import *


print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')


reset()


rounds_num = len(clubs) * (len(clubs) -1)








for i in range(0, len(clubs), 2):
    fixtures.append(Fixture(i, i+1))







for i in range(0, len(fixtures)):

    print(f'{fixtures[i].home.name} - {fixtures[i].away.name}')



print(len(fixtures))

 
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





# for i in range(0, len(fixtures)):

#     print(f'{fixtures[i].home.name} - {fixtures[i].away.name}')
#     print(f'{fixtures[i].home_odds} - {fixtures[i].draw_odds} - {fixtures[i].away_odds}')
#     print()

# input('Forduló szimulálása (Enter)')





