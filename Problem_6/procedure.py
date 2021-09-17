class procedures:
    def __init__(self,name,date,practioner,charges):
        self.__name = name
        self.__date = date
        self.__practioner = practioner
        self.__charges = charges
    #setters
    def setname(self, name):
        self.__name = name
    def setdate(self,date):
        self.__date = date
    def setpractioner(self, practioner):
        self.__practioner = practioner
    def setcharges(self, charges):
        self.__charges = charges
    #getters

    def getname(self):
        return self.__name
    def getdate(self):
        return self.__date
    def getpractioner(self):
        return self.__practioner
    def getcharges(self):
        return self.__charges
