
# Two pointer solution

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        max_water = 0
        while left < right:
            lower_line = height[left] if height[left] < height[right] else height[right]
            water = (right - left) * lower_line
            if water > max_water:
                max_water = water
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_water     