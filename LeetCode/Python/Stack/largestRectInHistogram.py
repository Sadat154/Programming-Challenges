def largestRectangleArea(heights):
    heights = [ (h,1) for h in (heights + [0])]
    stack = []
    max_area = 0

    for h, w in (heights):
        acc_w = 0
        print(stack, "1")
        while stack and stack[-1][0] >= h:
            print(stack)
            pH, pW = stack.pop()

            acc_w += pW
            max_area = max(max_area, (acc_w * pH))
            print(max_area)


        stack.append((h, acc_w+1))

            #
    return max_area






print(largestRectangleArea([1,1]))