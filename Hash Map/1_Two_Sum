

# Brute Force Solution
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]






# Hash Map Solution
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
        x = target - num
        if x in d:
            return [i, d[x]]
        elif num not in d:
            d[num] = i