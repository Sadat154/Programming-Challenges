from itertools import permutations

def createCombinations():
    userChoice = (input("Please choose the number of each letter with the nth arrangement, separated by spaces: "))
    userChoice = [x for x in userChoice.split(' ') if x.isnumeric()]
    userChoice = list(map(int,userChoice))


    finalString = ''.join(["A"*userChoice[0],"B"*userChoice[1],"C"*userChoice[2],"D"*userChoice[3]])


    combinations = sorted(list(set([''.join(x) for x in permutations(finalString)])))


    return combinations, userChoice

def calculateAnswer (userChoice, combinations):

    if userChoice[4] < len(combinations):
        print(combinations[userChoice[4]-1])
        print("Test 1")

    elif userChoice[4] == len(combinations):
        print(combinations[userChoice[4]-1])


    else:
        print(combinations[(userChoice[4] % len(combinations))-1])









if __name__ == "__main__":
    combinations, userChoice = createCombinations()

    calculateAnswer(userChoice,combinations)
