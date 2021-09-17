class patients:
    def __init__(self,name,middle_name,last_name,address,city,state,zipcode,phone,emergency_name,emergency_phone):
        self.__name = name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode= zipcode
        self.__phone = phone
        self.__emergency_name = emergency_name
        self.__emergency_phone = emergency_phone
    #setters
    def setname(self, name):
        self.__name = name
    def setlast(self, last_name):
        self.__last_name = last_name
    def setmiddle(self,middle_name):
        self.__middle_name = middle_name
    def setaddress(self, address):
        self.__address = address
    def setcity(self, city):
        self.__city = city
    def setstate(self,state):
        self.__state = state
    def setzipcode(self,zipcode):
        self.__zipcode= zipcode
    def setphone(self, phone):
        self.__phone = phone
    def setemergency_name(self,emergency_name):
        self.__emergency_name = emergency_name
    def setemergency_phone(self,emergency_phone):
        self.__emergency_phone = emergency_phone
    #getters
    def getname(self):
        return self.__name
    def getlast(self):
        return self.__last_name
    def getmiddle(self):
        return self.__middle_name
    def getaddress(self):
        return self.__address
    def getcity(self):
        return self.__city
    def getstate(self):
        return self.__state
    def getzipcode(self):
        return self.__zipcode
    def getphone(self):
        return self.__phone
    def getemergency_name(self):
        return self.__emergency_name
    def getemergency_phone(self):
        return self.__emergency_phone
