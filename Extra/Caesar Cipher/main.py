def encryption(key, plaintext):


    ciphertext = ""



    for char in plaintext:
        result = ((ord(char)+key))

        if result > 90 and char.isupper():
            ciphertext += chr((result-26))

        elif result >122 and char.islower():
            ciphertext += chr((result - 26))

        else:
            ciphertext += chr(result)

    return ciphertext




def decryption (key, ciphertext):
    plaintext = ""

    for char in ciphertext:
        result = ((ord(char) - key))
        if result < 65 and char.isupper():
            plaintext += chr((result+26))
        elif result < 97 and char.islower():
            plaintext += chr((result + 26))
        else:
            plaintext += chr(result)

    return plaintext

if __name__ == "__main__":

    text = input("Please enter the string you would like to be encrypted/decrypted: ")
    choice = input("Would you like your text to be encrypted or decrypted or brute? ('E' or 'D' or 'B') ").upper()
    if choice != "B":
        key_choice = int(input("Please enter your key: "))

        key_choice %= 26


    if choice == "E":
        print(encryption(key_choice,text))
    elif choice == "B":
        for i in range (1,27):
            print(f"{i}  {decryption(i, text)}")
    else:
        print(decryption(key_choice, text))