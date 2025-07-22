def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If we hit a duplicate, shrink the window from the left
        print(char_set, "1")
        while s[right] in char_set:
            print(char_set, "2")
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


s = "zxyzxyz"

print(lengthOfLongestSubstring(s))