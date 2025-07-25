from itertools import permutations
import math

def subsets(nums):
    res = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return


        # include nums[i
        subset.append(nums[i])
        dfs(i+1)

        # dont include nums [i
        subset.pop()
        dfs(i+1)

    dfs(0)

    return res



print(subsets([1, 2, 3]))