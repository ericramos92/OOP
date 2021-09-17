class informations:
    def __init__(self,name,address, age,phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
        #setters
    def setname(self, name):
        self.__name = name
    def setaddress(self, address):
        self.__address = address
    def setage(self, age):
        self.__age = age
    def setphone_number(self, phone_number):
        self.__phone_number = phone_number
    #getters
    def getname(self):
        return self.__name
    def getaddress(self):
        return self.__address
    def getage(self):
        return self.__age
    def getphone_number(self):
        return self.__phone_number
