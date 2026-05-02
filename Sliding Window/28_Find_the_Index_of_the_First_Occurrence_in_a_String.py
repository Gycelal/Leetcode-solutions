# O(m * n) Time and O(m) Space, where m is the length of the haystack and n is the length of the needle

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        l, r = 0, len(needle) - 1

        while r < len(haystack):
            if needle == haystack[l:r+1]:
                return l
            else:
                l += 1
                r += 1

        return -1