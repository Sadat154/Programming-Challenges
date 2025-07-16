def maxProduct(nums):
    if not nums:
        return 0

    # Initialize DP variables
    n = len(nums)
    max_dp = [0] * n  # max product ending at i
    min_dp = [0] * n  # min product ending at i

    # Base case
    max_dp[0] = min_dp[0] = result = nums[0]

    for i in range(1, n):
        num = nums[i]

        # Either the current number itself,
        # or extend the product from previous
        max_dp[i] = max(num, num * max_dp[i-1], num * min_dp[i-1])
        min_dp[i] = min(num, num * max_dp[i-1], num * min_dp[i-1])

        result = max(result, max_dp[i])

    return result