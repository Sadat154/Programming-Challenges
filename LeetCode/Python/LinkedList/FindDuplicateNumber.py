def findDuplicate(nums):
    for i in range(len(nums)):
        index = abs(nums[i])
        if nums[index - 1] < 0:
            return index
        nums[index - 1] *= -1