
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for start in range(len(haystack) - len(needle) + 1):

            j = 0

            while j < len(needle) and haystack[start + j] == needle[j]:
                j += 1

            if j == len(needle):
                return start

        return -1