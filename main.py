from club import Club
from sim import *
import os, random

os.system('cls')

clubs: list[Club] = []





f = open('clubs.csv', 'r', encoding='utf-8')
f.readline()
for row in f:
    clubs.append(Club(row))
f.close()

home = clubs[0]
away = clubs[8]

print(f'{home.name} - {away.name} ({home.power_ranking} - {away.power_ranking})')

probs = probs_calc(home.power_ranking, away.power_ranking)

print(probs)

# print(f'H {(probs[0]):.2f}')
# print(f'D {(probs[1]):.2f}')
# print(f'A {(probs[2]):.2f}')

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

