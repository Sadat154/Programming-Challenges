def characterReplacement(s, k):
    chardict = {}
    max_count = 0
    max_len = 0
    left = 0

    for right in range(len(s)):
        chardict[s[right]] = chardict.get(s[right], 0) + 1
        max_count = max(max_count, chardict[s[right]])

        # If the window size minus the count of the most frequent char is greater than k, shrink from left
        if (right - left + 1) - max_count > k:
            chardict[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

s = "AAABABB"
k = 1


print(characterReplacement(s,k))