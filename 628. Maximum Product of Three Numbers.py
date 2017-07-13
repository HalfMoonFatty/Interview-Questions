'''
Problem:

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''


'''
Solution: 线性遍历 时间复杂度O(n)

变量na, nb存储最小元素，变量pa, pb, pc存储最大元素

取 pa * na * nb,  pa * pb * pc的最大值
'''


import sys
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = pa = pb = pc = None
        na = nb = sys.maxint
        for n in nums:
            if n > pa: pa, pb, pc = n, pa, pb
            elif n > pb: pb, pc = n, pb
            elif n > pc: pc = n
            if n < na: na, nb = n, na
            elif n < nb: nb = n
        return max(ans, pa * na * nb, pa * pb * pc)
