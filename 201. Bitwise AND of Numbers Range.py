"""
Problem:

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
For example, given the range [5, 7], you should return 4.
"""

'''
Solution:

Find the leftmost common digits of m and n, padding zeros after that.
E.g. m=1110110, n=1110101， the leftmost common digits of m and n are 11101 padding zeros after the leftmost common digits. Thus, the answer is 1110100.

Time: O(n)??
Space: O(1)
'''


class Solution(object):
    def rangeBitwiseAnd(self, m, n):

        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p
