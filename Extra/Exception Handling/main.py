operatorsDict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y

}


def validateInputs():
    try:
        numInput = int(input("Please enter a natural number: "))
        operator = input("Please enter an operator: ")

        if numInput < 0:
            raise ValueError
        if operator not in operatorsDict:
            raise TypeError
    except TypeError:
        print("Incorrect Operator")
        validateInputs()

    except ValueError:
        print("Incorrect Natural Number")
        validateInputs()
    else:
        createTable(numInput, operator)


def createTable(numInput, operator):
    firstLineArray = [x for x in range(numInput + 1)]
    firstLineArray = [str(i) for i in firstLineArray]

    print(f"{operator} | {' '.rjust(4, ' ').join(firstLineArray)}")
    test = []

    for i in range(numInput + 1):
        for j in range(numInput + 1):
            try:
                test.append(operatorsDict[operator](i, j))
            except:
                test.append("-")
        for n in range(len(test)):
            try:
                if test[n].isdigit() == True:
                    test[n] = round(test[n], 1)
            except:
                if isinstance(test[n], float) == True:
                    test[n] = round(test[n], 1)

        test = ' '.rjust(4, ' ').join([str(l) for l in test])
        print(f"{i} | {test}")
        test = []


if __name__ == "__main__":
    validateInputs()