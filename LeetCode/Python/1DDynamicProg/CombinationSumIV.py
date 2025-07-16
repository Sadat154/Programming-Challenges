def combinationSum4(nums, target):
    memo  = {0 : 1}

    for total in range(1, target + 1):
        memo[total] = 0
        for num in nums:
            memo[total] += memo.get(total-num,0)

    return memo[target]
print(combinationSum4([3,1,2], 4))
print(combinationSum4([1], 3))


