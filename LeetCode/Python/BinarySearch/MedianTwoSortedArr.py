class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2  # Mid val of left parti
            j = half - i

            maxLeftA = A[i - 1] if i > 0 else float('-inf')
            minRightA = A[i] if i < m else float('inf')

            maxLeftB = B[j - 1] if j > 0 else float('-inf')
            minRightB = B[j] if j < n else float('inf')

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # Perfect partition found
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = i - 1  # move partition A left
            else:
                left = i + 1  # move partition A right


#Redo cheated too much