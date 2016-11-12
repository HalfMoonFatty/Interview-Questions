'''
Problem:

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


# Time: O(max(n,m))
# Space: O(max(n,m)+1)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        index1, index2 = len(a)-1, len(b)-1
        carry = 0
        res = ''
        
        while not (index1 < 0 and index2 < 0):
            val1 = 0 if index1 < 0 else int(a[index1])
            val2 = 0 if index2 < 0 else int(b[index2])
            val = val1 + val2 + carry
            carry = val/2
            val %= 2  # note

            res =str(val)+res
            index1 -= 1
            index2 -= 1
 
        return '1'+res if carry == 1 else res
        
