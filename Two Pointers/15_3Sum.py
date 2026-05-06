




class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for ind, num in enumerate(nums):
            if ind > 0 and num == nums[ind-1]:
                continue
            left = ind + 1
            right = len(nums) - 1
            while left < right:
                ThreeSum = num + nums[left] + nums[right]
                if ThreeSum < 0:
                    left += 1
                elif ThreeSum > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        
        return res
            