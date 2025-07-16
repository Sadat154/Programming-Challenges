
def subsetXORSum(nums):
    if not nums:
        return 0

    result = 0

    subset = []

    def dfs(i):
        nonlocal result
        if i == len(nums):
            xorr = 0
            for num in subset:
                xorr ^= num
            result += xorr
            return

        subset.append(nums[i])
        dfs(i+1)

        subset.pop()
        dfs(i+1)



    dfs(0)
    return result


print(subsetXORSum([3,1,1]))