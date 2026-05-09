# Brute Force solution O(n^2) time complexity and O(n) space complexity

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        longest_string = 0
        
        for i in range(n):
            sub = set()
            sub.add( s[i])
            for j in range(i+1, n):
                if s[j] not in sub:
                    sub.add(s[j])
                else:
                    break
            longest_string = max(len(sub), longest_string)
        return longest_string 
    

# Sliding Window solution O(n) time complexity and O(n) space complexity  


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        sub = set()
        max_length = 0
        while right < len(s):
            if s[right] not in sub:
                sub.add(s[right])
                max_length = max(max_length, len(sub))
                right += 1
            else:
                while s[right] in sub:
                    sub.remove(s[left])
                    left += 1
        return max_length

