from random import randint

class Timeline:
    baseyear = 1991
    ym1 = 0
    ym2 = 0
    ym3 = 0
    
    
    
    def generateMission(self):
        self.ym1 = randint(1969, 1990)
        self.ym2 = randint(1969, 1990)
        self.ym3 = randint(1969, 1990)
        print("Mission one happen in : ", self.ym1)
        print("Mission two happen in : " , self.ym2)
        print("Mission three happen in : " , self.ym3)
