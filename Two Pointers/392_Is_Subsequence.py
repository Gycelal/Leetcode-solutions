

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sp = 0
        tp = 0
        while sp < len(s):
            if tp > len(t) - 1:
                return False
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
        return True