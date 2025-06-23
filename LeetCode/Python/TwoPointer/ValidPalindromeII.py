def validPalindrome(s):

    pointer1 = 0
    pointer2 = len(s) - 1
    skipped=0
    false1 = 1
    false2 = 1

    while pointer1 < pointer2:
        if s[pointer1] == s[pointer2]:
            pointer1 += 1
            pointer2 -= 1

        else:
            #Check if we can skip the left pointer adn then still valid
            pointer1+=1
            while pointer1 < pointer2:
                if s[pointer1] != s[pointer2]:
                    pointer1 += 1
                    pointer2 -= 1
                else:
                    false1 = 0
                    break
            pointer1-=1
            pointer2-=1
            while pointer1 < pointer2:
                if s[pointer1] == s[pointer2]:
                    pointer1 += 1
                    pointer2 -= 1
                else:
                    false2 = 0
                    break

    if false1 == 1 or false2 == 1:
        return True
    return False

            #check if we can skip the right pointer and still valid





print(validPalindrome("abaa"))



#Bwetter sol
# p1 = 0
# p2 = len(s) - 1
# while p1 <= p2:
#     if s[p1] != s[p2]:
#         string1 = s[:p1] + s[p1 + 1:]
#         string2 = s[:p2] + s[p2 + 1:]
#         return string1 == string1[::-1] or string2 == string2[::-1]
#     p1 += 1
#     p2 -= 1
# return True