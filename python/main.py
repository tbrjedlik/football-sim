from fixture import Fixture
import os
from club import clubs

os.system('cls')

fixtures: list[Fixture] = []


for i in range(0, len(clubs), 2):
    fixtures.append(Fixture(i, i+1))    
    


# for i in range(0, len(fixtures)):

#     print(f'{fixtures[i].home.name} - {fixtures[i].away.name}')
#     print(f'{fixtures[i].home_odds} - {fixtures[i].draw_odds} - {fixtures[i].away_odds}')
#     print()

# input('Forduló szimulálása (Enter)')

# for i in range(0, len(fixtures)):

#     print(f'{fixtures[i].home.name} - {fixtures[i].away.name}')
#     print(f'{fixtures[i].simulating_result()}')
#     print()




