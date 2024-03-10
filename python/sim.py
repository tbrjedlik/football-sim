from club import clubs

def prob_to_odd(prob:float) -> float:
    odd = 1 / prob
    return odd

points = dict()
for c in clubs:
    points[c.abbr] = 0