def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    memo = [[-1] * (target + 1) for _ in range(n + 1)]
    print(memo)


    def dfs(i, target):
        if target == 0:
            return True

        if i >= n or target < 0:
            return False

        if memo[i][target] != -1:
            return memo[i][target]

        memo[i][target] = (dfs(i + 1, target - nums[i]) or dfs(i + 1, target))

        return memo[i][target]



    return dfs(0, target)
print(canPartition([1,2,3,4]))
print(canPartition([1,2,3,4,5]))

#Watch the hash set video oon this