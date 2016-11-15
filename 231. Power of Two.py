'''
Problem:

     Given an integer, write a function to determine if it is a power of two.

'''


'''
Solution: tricky solution

For any number n, if it is a power of 2, then the number that is 1 less than n (m = n-1) will have opposite '1' bit and '0' bits of n!!!
Apply "&" operation on "m" and "n" check if the result is '0'

Examples:

          8 = 1000
    &     7 = 0111
    -----------------
          0 = 0000

         9 = 1001
    &    8 = 1000
    -----------------
             1000

'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
            :type n: int
            :rtype: bool
            """
        if n <= 0: return False
        return (n&(n-1)) == 0
