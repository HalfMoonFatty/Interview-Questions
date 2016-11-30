'''
Problem:

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''


'''
Solution:

    利用位运算来消除重复3次的数。以一个数组[14 14 14 9]为例，将每个数字以二进制表达：

    1110
    1110
    1110
    1001
    _____
    4331    对每一位进行求和
    1001    对每一位的和做%3运算，来消去所有重复3次的数
'''


class Solution(object):
    def singleNumber(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        res = 0
        for i in range(31,-1,-1):
            mask = 1<<i
            sums = 0
            for n in nums:
                if n & mask:  
                    sums += 1
            res = (res<<1) + (sums%3)
            
        if res & 0x80000000:
            return -(res ^ 0xFFFFFFFF ) -1  #negative: 2's complement
        else:
            return res

        
# To convert an int to unsigned int in Python:
# a = A[i] & 0xffffffff
