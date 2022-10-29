

def validation():
    while True:
        try:
            card_number = input("Please enter a card number: ")
            if card_number.isdigit() == False:
                raise ValueError
            if len(card_number) != 16:
                raise TypeError

        except ValueError:
            print("Please ensure only numbers are input!")
        except TypeError:
            print("Please ensure a 16 digit card number is entered!")

        else:
            return card_number


def card_issuer(cardnumber):

    if cardnumber[0] == "3":
        if cardnumber[1] == "4" or cardnumber[1] == "7":
            print("The Card issuer is: American Express")
        else:
            print("The Card issuer is: JCB")
    elif cardnumber[0] == "4":
        print("The Card issuer is: Visa")
    elif cardnumber[0] == "5" and (6 > int(cardnumber[1]) > 0):
        print("The Card issuer is: Mastercard")
    else:
        print("No card issuer associated with this number!")
        exit()

def real_or_not(cardnum):

    digits = [int(x) for x in cardnum]
    even_digits = (digits[-2::-2])
    double = [x*2 for x in even_digits]
    odd_digits = (digits[-1::-2])

    checksum = 0
    checksum += sum(odd_digits)

    for i in double:
        checksum += sum([int(x) for x in str(i)])
    if checksum % 10 == 0:
        return "Valid Card Number"
    else:
        return "Invalid Card Number"

if __name__ == "__main__":
    card_num = validation()
    PAN = card_num[6:15]
    checksum = card_num[-1]
    card_issuer(card_num)

    print(real_or_not(card_num))