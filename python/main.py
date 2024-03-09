from club import Club
from sim import *
import os

os.system('cls')

clubs: list[Club] = []


f = open('python/clubs.csv', 'r', encoding='utf-8')
f.readline()
for row in f:
    clubs.append(Club(row))
f.close()

if len(clubs) % 2!= 0:
    raise Exception('Nem lehet páratlan számú csapat!')


def football_match(home_num:int, away_num:int):

    home = clubs[int(home_num)]
    away = clubs[int(away_num)]

    print(f'{home.name} - {away.name}')

    probs = probs_calc(home.power_ranking, away.power_ranking)
    
    print(f'H {prob_to_odd(probs[0]):.2f}')
    print(f'D {prob_to_odd(probs[1]):.2f}')
    print(f'A {prob_to_odd(probs[2]):.2f}')

    match probs_to_results(probs):
        case 'H':
            print(f'Győztes: {home.name}')
        case 'D':
            print(f'Döntetlen')
        case 'A':
            print(f'Győztes: {away.name}')
            
    print('\n')


def round():
    
    for i in range(0, len(clubs), 2):
        football_match(i, i+1)


            
            
round()