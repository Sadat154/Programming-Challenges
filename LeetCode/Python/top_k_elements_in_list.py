class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        unique = set(nums)
        x = sorted([[nums.count(i), i] for i in unique], reverse=True)
        finalAns = []

        for i in range(k):
            finalAns.append(x[i][1])
        return finalAns



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