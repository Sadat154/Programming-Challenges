operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y,
    '**': lambda x, y: x ** y
}
def validation():
    while True:
        try:
            calculation = input("Please Enter the number: ")

            if len(calculation.split(" ")) != 3:
                raise TypeError and ValueError

            if calculation.split(" ")[2] not in operators:
                raise TypeError
            if calculation.split(" ")[1].isdigit() == False or calculation.split(" ")[0].isdigit() == False:
                raise ValueError

        except TypeError:
            print("Incorrect Operator!")

        except ValueError:
            print("Please enter numbers for the first two choices!")


        else:
            calculator(calculation)
            break




def calculator(choice):
    print(f"{operators[choice.split(' ')[2]](int(choice.split(' ')[0]),int(choice.split(' ')[1]))}")

if __name__ == "__main__":

    validation()