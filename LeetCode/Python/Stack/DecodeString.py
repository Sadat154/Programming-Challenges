def decodeString(s):
    numStack = []
    charStack = []
    bracketsStack = []
    result = ""

    idx = 0

    while idx < len(s):
        if s[idx] == '[':
            bracketsStack.append('[')
            charStack.append("")  # push a new empty string for nested level
            idx += 1
            continue

        if s[idx].isdigit():
            num = 0
            while idx < len(s) and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1
            numStack.append(num)
            continue

        if s[idx] == ']':
            bracketsStack.pop()
            segment = charStack.pop()
            repeat = numStack.pop()
            expanded = segment * repeat

            if charStack:
                charStack[-1] += expanded  # append to outer level
            else:
                result += expanded  # if top level

            idx += 1
            continue

        if bracketsStack and s[idx].isalpha():
            charStack[-1] += s[idx]
            idx += 1
            continue

        if s[idx].isalpha() and not bracketsStack:
            result += s[idx]
            idx+=1



    return(result)



print(decodeString("ab2[c]3[d]1[x]"))
print(decodeString("axb3[z]4[c]"))
print(decodeString("2[a3[b]]c"))
