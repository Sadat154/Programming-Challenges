class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if (x) in numMap:
                return [numMap[target - nums[i]], i]



