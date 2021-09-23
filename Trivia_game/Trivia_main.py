import questions_class
questions_answers =['obj1','obj2','obj3','obj4','obj5','obj6','obj7','obj8','obj9','obj10']
for i in range(len(questions_answers)):
    questions_answers[i] = questions_class.questions('question','answer1','answer2','answer3','answer4')
    question = input(str(i+1)+"-Question:")
    ans1= input('answer A:')
    ans2= input('answer B:')
    ans3= input('answer C:')
    ans4= input('answer D:')
    questions_answers[i].setquestions(question)
    questions_answers[i].setanswer1(ans1)
    questions_answers[i].setanswer2(ans2)
    questions_answers[i].setanswer3(ans3)
    questions_answers[i].setanswer4(ans4)
counter = 1

for i in range(len(questions_answers)):
    #print menu
    print(questions_answers[i])
    if counter == 1:
        print("----------------------------------")
        print("Player 1:")
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'A':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1

    elif counter == 2:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'B':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1

    elif counter == 3:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'C':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
    elif counter == 4:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'D':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
    elif counter == 5:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'D':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1


        print("----------------------------------")
        print("Player 2:")
    elif counter == 6:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'A':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
    elif counter == 7:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'B':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
    elif counter == 8:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'C':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
    elif counter == 9:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'D':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
    elif counter == 10:
        player1_answer = input("Pick your answer:")
        if player1_answer.upper() == 'D':
            questions_answers[i].setcorrect_ans()
            print("You got it right")
        else:
            print("Wrong answer")
        counter +=1
player1 = questions_answers[0].getcorrect_ans() +  questions_answers[1].getcorrect_ans()+ questions_answers[2].getcorrect_ans()+ questions_answers[3].getcorrect_ans()+questions_answers[4].getcorrect_ans()
player2 = questions_answers[5].getcorrect_ans() +  questions_answers[6].getcorrect_ans()+ questions_answers[7].getcorrect_ans()+ questions_answers[8].getcorrect_ans()+questions_answers[9].getcorrect_ans()
print("SCORES FOR BOTH PLAYERS")
print("-----------------------")
print("Player1:" + str(player1))
print("Player2:" + str(player2))
if player1 > player2:
    print("PLAYER ONE IS THE WINNER")
else:
    print("PLAYER TWO IS THE WINNER")
