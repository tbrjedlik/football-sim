class Club:
    def __init__(self, row) -> None:
        
        data = row.strip().split(';')
        
        self.name = data[0]
        self.abbr = data[1]
        self.power_ranking = float(data[2])