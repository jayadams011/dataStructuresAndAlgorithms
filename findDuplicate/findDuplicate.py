def findDuplicate(nums):
    nums.sort()
    for i in nums:
        if nums[i] == nums[i-1]:
            return nums[i]


nums = [1, 3, 4, 3, 6, 5, 6]
