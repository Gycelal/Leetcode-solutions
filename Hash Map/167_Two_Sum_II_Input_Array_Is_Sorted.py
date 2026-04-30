
# Solution using Hash Map
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for ind, num in enumerate(numbers):
            x = target - num
            if x in d:
                return [d[x] + 1, ind+1]
            else:
                d[num] = ind
