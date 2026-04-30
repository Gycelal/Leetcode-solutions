# Two Pointer Solution

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        last = len(numbers) - 1

        while first < last:
            total = numbers[first] + numbers[last]
            if total == target:
                return [first + 1, last + 1]
            if total > target:
                last -= 1
            else:
                first += 1
