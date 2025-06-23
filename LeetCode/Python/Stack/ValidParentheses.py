def isValid(s):
    stack = []
    dictPar = { ")":"(", "]":"[", "}":"{"}

    if len(s) <= 1:
        return False

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if len(stack) == 0 or stack.pop() != dictPar[char]:
                return False
    if len(stack) == 0:
        return True
    return False