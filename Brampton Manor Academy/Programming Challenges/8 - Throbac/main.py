
def roman_to_int(romanInput):
    romanDict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,

    }
    position = 0
    counter = 0

    while position < len(romanInput):
        if (position + 1) < len(romanInput) and romanInput[position:position+2] in romanDict:
            counter += romanDict[romanInput[position:position+2]]
            position += 2
        else:
            counter += romanDict[romanInput[position]]
            position += 1

    return counter

def int_to_roman(digitalSum):
    numbers = [1,4,5,9,10,40,50,90,100]
    romanNumeral = ["I","IV","V","IX","X","XL","L","XC","C"]

    finalRomanValue =""

    i = 8


    while digitalSum > 0:
        quotient = digitalSum // numbers[i]

        digitalSum = digitalSum % numbers[i]

        while quotient > 0:
            finalRomanValue += romanNumeral[i]
            quotient -=1
        i -= 1

    return finalRomanValue

def run():
    romanNum1 = input("Enter First Roman Number (no spaces): ").upper()
    print(f"Value of {romanNum1} is: {roman_to_int(romanNum1)}")
    romanNum2 = input("Enter Second Roman Number (no spaces): ").upper()
    print(f"Value of {romanNum2} is: {roman_to_int(romanNum2)}")
    print(f"Sum of the Roman Numbers is: {roman_to_int(romanNum2) + roman_to_int(romanNum1)}")
    print(f"{roman_to_int(romanNum2) + roman_to_int(romanNum1)} in Roman Numerals is: {int_to_roman(roman_to_int(romanNum2) + roman_to_int(romanNum1))}")

if __name__ == "__main__":
    run()