def tribonacci(n):
    T0 = 0
    T1 = 1
    T2 = 1

    dp = [0] * (n+1)
    dp[0] = T0
    dp[1] = T1
    dp[2] = T2

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]


    return dp[-1]




print(tribonacci(3))
print(tribonacci(21))