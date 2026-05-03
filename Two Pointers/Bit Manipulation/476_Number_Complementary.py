
# Solution using binary conversion and string manipulation
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_rep = str(bin(num)[2:]) 
        new = "" 
        for num in bin_rep:
            if num == "0":
                 new += "1" 
            else: 
                new += "0"
        return int(new, 2)





# Solution using bit manipulation
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
        





















class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = (1 << num.bit_length()) - 1
        return num ^ mask