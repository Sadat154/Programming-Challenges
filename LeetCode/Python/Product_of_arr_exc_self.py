def productExceptSelf(nums):
    answer = []
    n = len(nums)

    prefix = [1] * n


    for i in range(1,n):
        prefix[i] = prefix [i - 1] * nums[i-1]

    suffix = [1] * n
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Step 3: Final result
    result = [prefix[i] * suffix[i] for i in range(n)]

productExceptSelf([4,3,2,1])