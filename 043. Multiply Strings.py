'''
Problem:

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
            :type num1: str
            :type num2: str
            :rtype: str
            """
        prod = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                prod[i+j+1] += int(num1[i])*int(num2[j])
        
        carry = 0
        for i in range(len(prod)-1,-1,-1):
            val = prod[i]+carry
            prod[i] = val%10
            carry = val/10
            
        
        ret = ''.join(str(x) for x in prod).lstrip('0')
        return ret if ret else '0'

