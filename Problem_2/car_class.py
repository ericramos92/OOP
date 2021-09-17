class cars:
    def __init__(self, year, make):
        self.year = year
        self.make = make
        self.speed = 0
    def setyear(self,year):
        self.year = year
    def setmake(self, year):
        self.make =make
    def setspeed(self):
        self.speed = 0
    def getyear(self):
        return self.year
    def getmake(self):
        return self.make
    def getspeed(self):
        return self.speed
    #other methods
    def setaccelerate(self):
        self.speed += 5
    def setbrake(self):
        self.speed -= 5
