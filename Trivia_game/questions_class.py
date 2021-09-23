class questions:
    def __init__(self,question,answer1,answer2,answer3,answer4):
        self.__correct_ans = 0
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        #setters
    def setquestions(self,question):
        self.__question = question
    def setanswer1(self,answer1):
        self.__answer1 = answer1
    def setanswer2(self,answer2):
        self.__answer2 = answer2
    def setanswer3(self,answer3):
        self.__answer3 = answer3
    def setanswer4(self,answer4):
        self.__answer4 = answer4
    def setcorrect_ans(self):
        self.__correct_ans += 1
        if self.__correct_ans == 5:
            self.__correct_ans = 0
        #getters
    def getquestion(self):
        return self.__question
    def getanswer1(self):
        return self.__answer1
    def getanswer2(self):
        return self.__answer2
    def getanswer3(self):
        return self.__answer3
    def getanswer4(self):
        return self.__answer4
    def getcorrect_ans(self):
        return self.__correct_ans
        #display
    def __str__(self):
        return str(self.__correct_ans + 1) +self.__question + \
                '\n A:' + self.__answer1 + \
                '\n B:' + self.__answer2 + \
                '\n C:' + self.__answer3 + \
                '\n D:' + self.__answer4
