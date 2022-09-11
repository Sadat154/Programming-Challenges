Test = 0

while Test == 0:
    answer = int(input("*You* This will be the answer. Please choose a number between 10 - 49: "))
    if answer >= 10 and answer <= 49:
        Test = 1
    else:
        Test = 0


while Test == 1:
    friendChoice = int(input("*Player* Pick a number between 50 - 99: "))
    if friendChoice >= 50 and friendChoice <= 99:
        Test = 2
    else:
        Test = 1

def factor(answer):
    factor = 99 - answer
    return factor

def calculations(answer, friendChoice):
    calcAns = factor(answer) + friendChoice

    calcAns = str(calcAns)
    FinalCalcAnswer = int(calcAns[0]) + int(calcAns[1:3])
    FinalCalcAnswer = friendChoice - FinalCalcAnswer
    return FinalCalcAnswer


print(f"I said the answer was {answer} and the calculation result is {calculations(answer,friendChoice)}")

