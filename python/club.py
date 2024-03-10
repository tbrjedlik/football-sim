class Club:
    def __init__(self, row) -> None:
        
        data = row.strip().split(';')
        
        self.name = data[0]
        self.abbr = data[1]
        self.power_ranking = float(data[2])
        
clubs: list[Club] = []

f = open('python/clubs.csv', 'r', encoding='utf-8')
f.readline()
for row in f:
    clubs.append(Club(row))
f.close()

if len(clubs) % 2!= 0:
    raise Exception('Nem lehet páratlan számú csapat!')