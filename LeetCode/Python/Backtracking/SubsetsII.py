def subsetsWithDupe(nums):
    res = []

    subset = []
    nums.sort()
    def dfs(i):

        if i == len(nums):
            if subset not in res:

                res.append(subset.copy())
            return


        subset.append(nums[i])
        dfs(i+1)

        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        subset.pop()
        dfs(i+1)



    dfs(0)

    return (res)
print(subsetsWithDupe([1,2,1]))
