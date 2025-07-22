def checkInclusion(s1,s2):
    if len(s1) > len(s2):
        return False
    s1_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1

    window_count = {}
    for i in range(len(s1)):
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1

    if window_count == s1_count:
        return True

    # slide window over s2
    for i in range(len(s1), len(s2)):
        left_char = s2[i - len(s1)]
        right_char = s2[i]

        #remove lef char
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]


        # add right char
        window_count[right_char] = window_count.get(right_char, 0) + 1

        if window_count == s1_count:
            return True

    return False



s1 = "abc"
s2 = "lecabee"
print(checkInclusion(s1,s2))