def lengthOfLIS(nums):
    n = len(nums)
    cache = {}

    def dfs(i):
        if i in cache:
            return cache[i]

        max_len = 1  # LIS ending at i is at least the element itself

        for j in range(i):
            if nums[i] > nums[j]:
                max_len = max(max_len, dfs(j) + 1)

        cache[i] = max_len
        return max_len

    return max(dfs(i) for i in range(n))





print(lengthOfLIS([9,1,4,2,3,3,7]))
print(lengthOfLIS([0,3,1,3,2,3]))