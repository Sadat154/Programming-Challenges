# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(set(nums)) < len(nums):
#             return True
#         else:
#             return False


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False




X = Solution()
X.containsDuplicate([1,23,11,1])
print(X)






