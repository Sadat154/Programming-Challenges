# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         unique = set(nums)
#         x = sorted([[nums.count(i), i] for i in unique], reverse=True)
#         finalAns = []
#
#         for i in range(k):
#             finalAns.append(x[i][1])
#         return finalAns
#
#
from collections import defaultdict


#
# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     heap = []
#     counter = {}
#     for n in nums:
#         counter[n] = 1 + counter.get(n, 0)
#
#     for key, val in counter.items():
#         heapq.heappush(heap, (-val, key))
#
#     res = []
#     while len(res) < k:
#         res.append(heapq.heappop(heap)[1])
#
#     return res
#Better solution

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         counter = {}
#         for num in nums:
#             counter[num] = 1 + counter.get(num, 0)
#
#         test = (sorted(counter.items(), key=lambda x: x[1], reverse=True))
#         return [i[0] for i in test[:k]]
#

x = Solution()
print(x.topKFrequent([2,2,3,4,1,1,2], 2)
)