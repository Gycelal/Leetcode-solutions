
""" Not the most efficient solution, but it works. We can optimize it by using two pointers and calculating the max
  left and max right on the fly instead of storing them in separate lists. o(n) time and o(n) space complexity. """
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        max_left = []
        max_right = []
        min_val = []
        water = 0
        for i in range(n):
            if not max_left:
                max_left.append(height[i])
            else:
                if height[i-1] > max_left[-1]:
                    max_left.append(height[i-1])
                else:
                    max_left.append(max_left[-1])
        for i in range(n-1, -1, -1):
            if not max_right:
                max_right.append(height[i])
            else:
                if height[i+1] > max_right[-1]:
                    max_right.append(height[i+1])
                else:
                    max_right.append(max_right[-1])
        max_right = max_right[::-1]
                    
        for i in range(len(height)):
            if max_left[i] < max_right[i]:
                min_val.append(max_left[i])
            else:
                min_val.append(max_right[i])
        for i in range(len(height)):
            if min_val[i] - height[i] > 0 :
                water += min_val[i] - height[i]
        return water
    

# Two Pointer Solution which has o(n) time and o(1) space complexity. We can calculate the max left and max right on the fly using two pointers.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        water = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                traped_water = leftMax - height[left]
                water += traped_water if traped_water > 0 else 0
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                traped_water = rightMax - height[right]
                water += traped_water if traped_water > 0 else 0
        return water

