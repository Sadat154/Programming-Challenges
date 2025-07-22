def maxProfit(prices):
    maxProfit = 0
    minVal = float('inf')


    for i in prices:
        if i < minVal:
            minVal = i

        maxProfit = max(maxProfit, i - minVal)

    return maxProfit









prices = [10,1,5,6,7,1]
print(maxProfit(prices))