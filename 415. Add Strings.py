'''
Problem:

Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index1, index2 = len(num1)-1, len(num2)-1
        carry = 0
        res = ''
        
        while not (index1 < 0 and index2 < 0):
            val1 = 0 if index1 < 0 else int(num1[index1])
            val2 = 0 if index2 < 0 else int(num2[index2])
            val = val1 + val2 + carry
            
            carry = val/10
            val %= 10  # note
            res =str(val)+res
            
            index1 -= 1
            index2 -= 1
        
        return '1'+res if carry == 1 else res
