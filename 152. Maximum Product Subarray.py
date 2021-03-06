'''
Problem:

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        ret = maxprod = minprod = nums[0]    # init
        
        for i in range(1,len(nums)):
            tmpmax = maxprod
            maxprod = max(nums[i],nums[i]*maxprod,nums[i]*minprod)
            minprod = min(nums[i],nums[i]*tmpmax,nums[i]*minprod)
            ret = max(ret,maxprod)
        return ret
            
