def maxArea(heights):
    left, right = 0, len(heights) - 1
    maxArea = 0

    while left < right:
        width = right - left
        maxArea = max(maxArea, width * (min(heights[left], heights[right])))

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return maxArea

print(maxArea([1,7,2,5,4,7,3,6]))