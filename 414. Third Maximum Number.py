'''
Problem:

Given an array of integers, return the 3rd Maximum Number in this array, if it doesn't exist, return the Maximum Number. 
The time complexity must be O(n) or less.
'''

'''
Solution:

Time: O(n)
Space: O(1)
'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = None
        for n in nums:
            if n > a:
                a,b,c = n,a,b
            elif a > n > b:
                b,c = n,b
            elif b > n > c:
                c = n
        return c if c is not None else a
                
