import random

def prob_to_odd(prob:float) -> float:
    odd = 1 / prob
    return odd

# home_ranking = 91.9
# away_ranking = 96.6

def probs_calc(home_ranking:float, away_ranking:float) -> list[float]:
    
    home_advantage = (random.randint(100, 120)) / (  away_ranking * (random.randint(70, 99)/100)  )
    
    expected_home = ( 1 / (1 + 10 ** ((away_ranking - home_ranking) /  random.randint(20,35)     )) ) * home_advantage
    expected_away = 1 / (1 + 10 ** ((home_ranking - away_ranking) / random.randint(20,35)    ))
    expected_draw = ( 1 / (1 + 10 ** ((home_ranking - away_ranking) / 35)) ) * (home_advantage * ( random.randint(6,10) / 10 ) )



    expected_results = [expected_home, expected_draw, expected_away]

    total = sum(expected_results)

    probs = []
    for num in expected_results:
        probs.append(num / total)

    # odds = []
    # for num in probs:
    #     odds.append(prob_to_odds(num))

    return probs

# probs = probs_calc(home_ranking, away_ranking)

# print(f'H {prob_to_odd(probs[0]):.2f}')
# print(f'D {prob_to_odd(probs[1]):.2f}')
# print(f'A {prob_to_odd(probs[2]):.2f}')


