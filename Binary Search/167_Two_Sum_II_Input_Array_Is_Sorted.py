# Binary Search Solution

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ind, num in enumerate(numbers):
            needed = target - num
            left = ind + 1
            right = len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == needed:
                    return [ind + 1, mid + 1]
                elif numbers[mid] < needed:
                    left = mid + 1
                elif numbers[mid] > needed:
                    right = mid - 1