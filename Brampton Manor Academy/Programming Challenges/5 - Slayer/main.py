
def results(slayer, layers):
    print(f"SLAYER + SLAYER + SLAYER = {int(slayer)*3}")
    print(f"LAYERS = {layers}")
    print("Thanks for playing.")

def checkSlayers(slayer, layers):

    threeSlayer = int(slayer) * 3
    if str(threeSlayer) != layers:
        print("Your guess is incorrect:")

    else:
        print("Your guess is correct:")

    results(slayer, layers)
    return threeSlayer


while True:
    slayer = input("Enter your guess for slayer: ")
    layers = slayer[1:] + slayer[0:1]

    if layers == str(checkSlayers(slayer,layers)):
        break
    else:
        True

