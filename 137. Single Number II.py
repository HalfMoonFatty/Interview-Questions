'''
Problem:

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

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
            # print "{0:b}".format(mask)
            sum = 0
            for j in range(len(nums)):
                if nums[j] & mask:      
                    sum += 1
            res = (res<<1) + (sum%3)

        if res & 0x80000000:
            return -(res ^ 0xFFFFFFFF ) -1  # negative: 2's complement
        else:
            return res

        
