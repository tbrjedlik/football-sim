from club import clubs
import os

def prob_to_odd(prob:float) -> float:
    odd = 1 / prob
    return odd

def reset():
    os.system('cls')

    if not os.path.exists('results'):
        os.makedirs('results')
    
    f = open('results/results.txt', 'w', encoding='utf-8')
    f.write('')
    f.close()

points = dict()
for c in clubs:
    points[c.abbr] = 0


