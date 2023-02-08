def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    x = 0
    nums = nums[-1::-1]
    length = len(nums)
    for num in range(length - 1):
        for j in range(length):
            count = length - 1
            nums[count] = num + nums[j]
            count = count - 1
    return nums[-1::-1]

print(runningSum([1, 2, 3, 4]))

