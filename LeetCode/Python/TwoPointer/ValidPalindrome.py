x = "Heeh?!:!"
def isPalindrome(s):
    newStr = ''.join(c.lower() for c in s if c.isalnum())

    forwardCounter = 0
    backwardCounter = len(newStr) - 1


    while forwardCounter < backwardCounter:
        if newStr[forwardCounter] == newStr[backwardCounter]:
            forwardCounter += 1
            backwardCounter -= 1
            continue
        else:
            return False
    return True



print(isPalindrome("Was it a car or a cat I saw?"))