from collections import deque

# O(n) time and O(k) space complexity solution using deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = deque()
        res = []

        for i in range(len(nums)):

            # Remove indices outside window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding results after first window
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res