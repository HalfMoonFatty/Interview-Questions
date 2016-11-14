'''
Problem:

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            count += (n>>i & 1)
        return count

    
    
class Solution:

    def hammingWeight(self, n):
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
