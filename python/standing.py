class Standing:
    def __init__(self, row) -> None:
        
        data = row.strip().split(';')
        
        self.abbr = data[0]
        self.points = data[1]

standings: list[Standing] = []

f = open('results/standings.csv', 'r', encoding='utf-8')
for row in f:
    standings.append(Standing(row))
f.close()