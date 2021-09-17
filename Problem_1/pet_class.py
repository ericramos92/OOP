class pets:
    def __init__(self,name,animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    def setname(self, name):
        self.__name = name
    def setanimaltype(self, animal_type):
        self.__animal_type = animal_type
    def setage(self,age):
        self.__age = age
    def getname(self):
        return self.__name
    def getanimaltype(self):
        return self.__animal_type
    def getage(self):
        return self.__age
