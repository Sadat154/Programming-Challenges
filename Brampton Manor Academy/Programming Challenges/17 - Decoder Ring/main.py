
def newDial(n, word):
    print(4%27)
    alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    encrypted_alphabet = []

    pos = 0

    while len(alphabets) != 0:
        pos += n -1
        pos = pos % len(alphabets)

        newans = alphabets[pos]

        alphabets.remove(newans)
        encrypted_alphabet.append(newans)





    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = ''


    test = 0
    for char in word:
        counter = alphabets.index(char) + test
        if counter+1 > 26:
            counter -= 26

        result += encrypted_alphabet[counter]
        test += 1




    print(encrypted_alphabet)


    print(result)

if __name__ == "__main__":
    newDial(999999, "MOON")