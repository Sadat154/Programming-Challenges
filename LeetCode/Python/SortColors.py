def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    count0 = 0
    count2 = 0

    for i in nums:
        if i == 0:
            count0 += 1
        elif i == 2:
            count2 += 1

    count1 = n - count0 - count2
    print(count1)
    i = 0
    while count2 != 0 or count1 != 0 or count0 != 0:
        if count0 >0:
            nums[i] = 0
            count0 -= 1
            i += 1
            print("!")
            continue

        if count1 > 0:

            nums[i] = 1
            count1 -= 1
            i += 1
            continue

        if count2 > 0:
            nums[i] = 2
            count2 -= 1
            i += 1
            continue

    return nums


print(sortColors([1,0,1,2]))