# def decodeString(s):
#     numStack = []
#     charStack = []
#     bracketsStack = []
#     result = ""
#
#     idx = 0
#
#     while idx < len(s):
#         if s[idx] == '[':
#             bracketsStack.append('[')
#             charStack.append("")  # push a new empty string for nested level
#             idx += 1
#             continue
#
#         if s[idx].isdigit():
#             num = 0
#             while idx < len(s) and s[idx].isdigit():
#                 num = num * 10 + int(s[idx])
#                 idx += 1
#             numStack.append(num)
#             continue
#
#         if s[idx] == ']':
#             bracketsStack.pop()
#             segment = charStack.pop()
#             repeat = numStack.pop()
#             expanded = segment * repeat
#
#             if charStack:
#                 charStack[-1] += expanded  # append to outer level
#             else:
#                 result += expanded  # if top level
#
#             idx += 1
#             continue
#
#         if bracketsStack and s[idx].isalpha():
#             charStack[-1] += s[idx]
#             idx += 1
#             continue
#
#         if s[idx].isalpha() and not bracketsStack:
#             result += s[idx]
#             idx+=1
#
#
#
#     return(result)
#
#
#
# print(decodeString("ab2[c]3[d]1[x]"))
# print(decodeString("axb3[z]4[c]"))
# print(decodeString("2[a3[b]]c"))
#
# print(1^7)
from collections import Counter


def minWindow(s, t):
    toCheck = Counter(t)
    left = 0
    have, need = 0, len(toCheck)
    currentMin = [0, 0, float('inf')]  # (left, right, length)
    freq = {}

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        if char in toCheck and freq[char] == toCheck[char]:
            have += 1


    while have == need:
        if (right - left + 1) < currentMin[2]:
            currentMin = [left, right, right - left + 1]

        freq[s[left]] -= 1
        if s[left] in toCheck and freq[s[left]] < toCheck[s[left]]:
            have -= 1
        left += 1




    return s[currentMin[0]:currentMin[1]+1] if currentMin[2] != float('inf') else ""


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

