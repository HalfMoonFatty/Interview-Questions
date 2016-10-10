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
        
        res = [0] * (max(len(num1),len(num2))+1)
        carry = 0
        i,j,k = len(num1)-1, len(num2)-1, len(res)-1
        
        while i >= 0 and j >= 0 and k >= 0:
            tmp = int(num1[i]) + int(num2[j]) + carry
            res[k] = tmp%10
            carry = tmp/10
            i -= 1
            j -= 1
            k -= 1
    
        while i >= 0 and k >= 0:
            tmp = int(num1[i]) + carry
            res[k] = tmp%10
            carry = tmp/10
            i -= 1
            k -= 1
        
        while j >= 0 and k >= 0:
            tmp = int(num2[j]) + carry
            res[k] = tmp%10
            carry = tmp/10
            j -= 1
            k -= 1   
            
        res[k] = carry
        ret = ''.join(str(x) for x in res).lstrip('0')  
        
        return ret if ret else '0'
