def letterCombinations(digits):

    keypad_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': [' ', '+'],
        '*': [],
        '#': []
    }

    res = []

    def backtrack(curStr, i):
        if len(curStr) == len(digits):
            res.append(curStr)
            return

        for char in keypad_map[digits[i]]:
            backtrack(curStr + char, i + 1)


    if digits:
        backtrack('', 0)

    return res

