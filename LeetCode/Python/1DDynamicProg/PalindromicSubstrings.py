def countSubstrings(s):
    count = 0

    def expandAroundCentre(left, right):
        nonlocal count, resLen, resStart
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1




    for i in range(len(s)):

        #even check
        expandAroundCentre(i, i+1)

        #odd check
        expandAroundCentre(i, i)

    return count



print(countSubstrings("abc"))
print(countSubstrings("aaa"))