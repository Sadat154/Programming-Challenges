def numDecodings(s):



    number_to_letter = {str(i + 1): chr(i + 65) for i in range(26)}
    n = len(s)

    dp = {len(s): 1}


    for i in range(len(s) -1, -1, -1):

        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and (s[i] == "1" or
                               s[i] == "2" and s[i + 1] in "0123456"
        ):
            dp[i] += dp[i + 2]
        return dp[0]





print(numDecodings('1012'))
print(numDecodings('12'))
print(numDecodings('01'))