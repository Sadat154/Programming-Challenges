def combinationSum2(candidates, target):
    n = len(candidates)
    res = []

    def dfs(i, current, subset):
        if current == target:
            res.append(subset[:])
            return

        if i >= n or current > target:
            return

        subset.append(candidates[i])
        dfs(i+1, current + candidates[i], subset)
        subset.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        # Exclude the current number and move to the next
        dfs(i + 1, current, subset)

    dfs(0, 0, [])

    return res


print(combinationSum2([9,2,2,4,6,1,5], 7))