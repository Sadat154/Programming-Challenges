def combinationSum(candidates, target):
    res = []

    def dfs(i, current, subset):
        if current == target:
            res.append(subset.copy())
            return
        if current > target or i >= len(candidates):
            return

        # Include the current number (can be reused)
        subset.append(candidates[i])
        dfs(i, current + candidates[i], subset)
        subset.pop()

        # Exclude the current number and move to the next
        dfs(i + 1, current, subset)

    dfs(0, 0, [])
    return res



print(combinationSum([2,5,6,9], 9))