class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        n = len(s)
        char_map = {}
        longest = 0
        while right < n:
            if s[right] not in char_map:
                char_map[s[right]] = 1
            else:
                char_map[s[right]] += 1
            w_length = (right - left) + 1
            max_char = max(char_map.values())
            if w_length - max_char <= k:
                longest = max(longest, w_length)
            else:
                char_map[s[left]] -= 1
                left += 1
            right += 1
        return longest    