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
    
    
    # print()
    # print()
    # print('   ________  ____  _________  ___   __   __     __________  ___')
    # print('  / __/ __ \/ __ \/_  __/ _ )/ _ | / /  / /    / __/  _/  |/  /')
    # print(' / _// /_/ / /_/ / / / / _  / __ |/ /__/ /__  _\ \_/ // /|_/ / ')
    # print('/_/  \____/\____/ /_/ /____/_/ |_/____/____/ /___/___/_/  /_/  ')
    # print()
    # print()

    # sleep(0.5)
    
    # input('CONTINUE >>> ')
    
    # os.system('cls')




