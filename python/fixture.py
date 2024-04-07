import math
from random import randint, uniform, random
from sim import prob_to_odd, points, played_games
from club import clubs

class Fixture:
    def __init__(self, home_num:int, away_num:int) -> None:
            self.home = clubs[int(home_num)]
            self.away = clubs[int(away_num)]

            self.home_advantage = (randint(100, 120)) / (  self.away.power_ranking * uniform(0.7, 0.99)  )
            self.expected_home = ( 1 / (1 + 10 ** ((self.away.power_ranking - self.home.power_ranking) /  randint(20,35)     )) ) * self.home_advantage
            self.expected_draw = ( 1 / (1 + 10 ** ((self.home.power_ranking - self.away.power_ranking) / 35)) ) * (self.home_advantage * ( uniform(0.6, 1.0) ) )
            self.expected_away = 1 / (1 + 10 ** ((self.home.power_ranking - self.away.power_ranking) / randint(20,35)    ))
            
            
            self.expected_results = [self.expected_home, self.expected_draw, self.expected_away]

            self.total = sum(self.expected_results)

            self.probs = []
            for num in self.expected_results:
                self.probs.append(num / self.total)
              
            self.home_prob = self.probs[0]
            self.draw_prob = self.probs[1]
            self.away_prob = self.probs[2]
            
            self.home_odds = round( prob_to_odd(self.home_prob) , 2)
            self.draw_odds = round( prob_to_odd(self.draw_prob) , 2)
            self.away_odds = round( prob_to_odd(self.away_prob) , 2)
            
            self.winner = None
            
    def simulating_result(self) -> str:
        if self.winner == None:
            n = 5
            
            played_games[self.home.abbr] += 1
            played_games[self.away.abbr] += 1
            
            home = int ( round(self.probs[0], n) * 10**(n+1) )
            draw = int ( round(self.probs[1], n) * 10**(n+1) )
            away = int ( round(self.probs[2], n) * 10**(n+1) )
            
            sum = home + draw + away
            
            winner = randint(1, sum)
            
            f = open('results/results.txt', 'a', encoding='utf-8')
            f.write(f'{self.home.abbr} - {self.away.abbr}\n')
            
            self.final_score = [0, 0]
            
            if winner in range(1, home+1):
                
                self.winner = self.home
                while self.final_score[0] <= self.final_score[1]:
                    self.final_score = self.goal_number_calc()
                    

            if winner in range(home+1, home+draw+1):
                self.final_score = [1, 0]

                self.winner = 'DRAW'
                while self.final_score[0] != self.final_score[1]:
                    self.final_score = self.goal_number_calc()

            else:

                self.winner = self.away
                while self.final_score[0] >= self.final_score[1]:
                    self.final_score = self.goal_number_calc()


            if self.winner == 'DRAW':
                points[self.home.abbr] += 1
                points[self.away.abbr] += 1
                f.write(f'Result: DRAW\n')
            else:
                points[self.winner.abbr] += 3
                f.write(f'Result: {self.winner.name.upper()}\n')

            f.write(f'---\n')
            f.close()

        
        else:
            raise Exception('Fixture already simulated')
        
    def goal_number_calc(self):
        
        def exponential_decay(distance, decay_rate=1.0):

            return math.exp(-decay_rate * distance)

        def draw_number(target_number, min_value, max_value, decay_rate=1.0):

            numbers = list(range(min_value, max_value + 1))

            probabilities = []
            
            for num in numbers:
                if num == target_number:

                    probabilities.append(2.0)
                else:

                    distance = abs(num - target_number)
                    

                    probability = exponential_decay(distance, decay_rate)
                    probabilities.append(probability)
                    total_probability = 0

            for p in probabilities:
                total_probability += p

            normalized_probabilities = [prob / total_probability for prob in probabilities]

            rand_val = random()
            cumulative_prob = 0.0
            
            for i in range(len(numbers)):
                cumulative_prob += normalized_probabilities[i]
                if rand_val < cumulative_prob:
                    return numbers[i]

        target_number = ( (self.home_odds + self.away_odds) / 2 ) * (self.home_odds / self.away_odds)

        min_value = 1
        max_value = 10
        decay_rate = 4
        
        goals = draw_number(target_number, min_value, max_value, decay_rate)





        n = 5
    
        p = self.probs[0]
        q = self.probs[2]
            
        normalized_p, normalized_q = p/(p+q), q/(p+q)
        
        home = int ( round( (normalized_p)**(1/goals) , n) * 10**(n+1) )
        away = int ( round( (normalized_q)**(1/goals) , n) * 10**(n+1) )
        
        sum = home + away
        
        self.home_score = 0
        self.away_score = 0
        
        for i in range(goals+1):
            goal = randint(1, sum)
            
            if goal in range(1, home+1):
                self.home_score += 1

            else:
                self.away_score += 1

        return self.home_score, self.away_score
    

class Match(Fixture):
    pass

class Rematch(Fixture):
    def __init__(self, home_num: int, away_num: int) -> None:
        super().__init__(away_num, home_num)

fixtures: list[Fixture] = []
matches: list[Fixture] = []
rematches: list[Fixture] = []

number_of_rounds = (len(clubs) - 1)*2
fixtures_num = int( (len(clubs) * (len(clubs)-1)) / 20 )


def fixture_maker(cs):
    for c in cs:
        pairing = []
        for i in range(0, int(len(cs)/2)):
            pairing.append([cs[i], cs[-1-i]])
    for p in pairing:
        matches.append(Match(p[0], p[1]))
        rematches.append(Rematch(p[0], p[1]))

def round_robin():

    club_index = []

    for i in range(0, len(clubs)):
        club_index.append(i)


    for i in range(0, fixtures_num):

        if i == 0:

            fixture_maker(club_index)
            
        else:
            
            club_index.insert(1, club_index[-1])
            club_index=club_index[0:len(club_index)-1]
            
            fixture_maker(club_index)



# FIX = Fixture(1, 2)
# print(f'{FIX.home.name} - {FIX.away.name}')
# print(f'{FIX.home_odds} | {FIX.draw_odds} | {FIX.away_odds}')
# FIX.simulating_result()
# print(FIX.final_score)
# try:
#     print(FIX.winner.name)
# except:
#     print('DRAW')