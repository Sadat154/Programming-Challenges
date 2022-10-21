def dictOfWords():

    wordDict = {}
    while True:
        try:
            word = input("Enter a word: ")

            if word.isalpha() == False:
                raise ValueError
        except ValueError:
            print("Please enter only alphabetical characters!")
        else:
            break


    

    for i in range(len(word)+1):
        for j in range(len(word)+1):
            if word[i:j] in wordDict:
                wordDict[word[i:j]] += 1
            else:
                wordDict[word[i:j]] = 1


    return wordDict






def calculateScore(dictCombination):
    KevinVowel = 0
    StuartConst = 0
    listOfWords = [x for x in dictCombination]

    for word in listOfWords:
        if word == '':
            continue
        if word[0:1] in 'aeiou':
            KevinVowel += dictCombination[word]
        else:
            StuartConst += dictCombination[word]

    if StuartConst > KevinVowel:
        print(f"Stuart {StuartConst}")
    elif KevinVowel > StuartConst:
        print(f"Kevin {KevinVowel}")
    else:
        print("Draw")








if __name__ == '__main__':
    dictOfCombinations = dictOfWords()
    calculateScore(dictOfCombinations)




