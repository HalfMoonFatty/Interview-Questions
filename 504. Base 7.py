'''
Problem:

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        
        ans = ''
        sign = 1 if num > 0 else -1
        n = abs(num)
        
        while n > 0:
            ans = str(n % 7) + ans
            n /= 7 
        return ans if sign == 1 else "-" + ans
