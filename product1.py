class Cection:
    def __init__(self):
        self.name = []
        self.option = []
        self.scoer = []
        
    def cection_up(self):
        self.name.append(input())
        self.option.append(input())
        self.scoer.append(input())
        
    def cection_ha(self):
        msg = self.name
        return msg
        
        
cection_1 = Cection()

cection_1.cection_up("iPhone", 30000, 30)
cection_1.cection_up("iPhone2", 30000, 30)
cection_1.cection_up("iPhone3", 30000, 30)

print(cection_1)