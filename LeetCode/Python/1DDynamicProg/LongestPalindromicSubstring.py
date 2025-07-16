def isPalindrome(s, i, j):
    if s[i:j+1] == s[i:j+1][::-1]:
        return True

def longestPalindrome(s):
    resLen = 0
    resStart = 0

    def expandAroundCenter(left, right):
        nonlocal resLen, resStart
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > resLen:
                resLen = right - left + 1
                resStart = left
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindrome
        expandAroundCenter(i - 1, i + 1)

        # Even-length palindrome
        expandAroundCenter(i, i + 1)

    return s[resStart:resStart + resLen]

print(longestPalindrome("abcabcbb"))
