def threeSum(nums):
    nums = sorted(nums)
    print(nums)

    solution = []

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            tempNums = nums.copy()
            tempNums.remove(nums[i])
            tempNums.remove(nums[j])
            if (nums[i]+nums[j])*-1 in tempNums:
                solution.append([nums[i],nums[j],(nums[i]+nums[j])*-1])
    print(solution)


threeSum([-1,0,1,2,-1,-4])

