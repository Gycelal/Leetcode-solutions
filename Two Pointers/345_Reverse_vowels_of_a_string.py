# O(n) time and O(n) space complexity solution

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        rev_vowels = []
        vowels = set('aeiouAEIOU')
        for char in s:
            if char in vowels:
                rev_vowels.append(char)
        res = []
        for char in s:
            if char in vowels:
                res.append(rev_vowels.pop())
            else:
                res.append(char)
        return "".join(res)
    

# Two pointer solution O(n) time and O(n) space complexity

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = set('aeiouAEIOU')
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return "".join(s_list)