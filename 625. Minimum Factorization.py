'''
Problem:


Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input: 48 
Output: 68

Example 2
Input: 15
Output: 35
'''

# Solution: 从9到2试除 如果有越大的数，那么counterpart一定是一个越小的数，最后把所有digit从小到大整合成result


class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1: return 1
        
        digit = [0] * 10
        for x in range(9, 1, -1):
            while a % x == 0:
                digit[x] += 1
                a /= x
        if a > 1: return 0   # 不能被因式分解
        
        ans = int(''.join(str(n) * digit[n] for n in range(2, 10)))
        return ans <= sys.maxint and ans or 0
