def coinChange(coins, amount):

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0
    for i in range(1,amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)


    return dp[amount] if dp[amount] != float('inf') else -1








print(coinChange([1,5,10], 12))
print(coinChange([2], 3))
print(coinChange([1], 0))
