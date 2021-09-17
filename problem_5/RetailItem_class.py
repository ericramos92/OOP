class retailitems:
    def __init__(self, description,units,prices):
        self.__description= description
        self.__units = units
        self.__prices = prices
    #setters
    def setdescription(self , description):
        self.__description = description
    def setunits(self ,units):
        self.__units = units
    def setprices(self , prices):
        self.__prices = prices
    #getters
    def getdescription(self):
        return self.__description
    def getunits(self):
        return self.__units
    def getprices(self):
        return self.__prices
