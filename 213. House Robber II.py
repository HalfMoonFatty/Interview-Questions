
'''
Problem:

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''

# 将环形DP问题转化为两趟线性DP问题

class Solution:

    def rob(self, nums):

        def robHelper(nums):
            if len(nums) < 1:
                return 0

            dp = [0] * (len(nums)+1)
            dp[1] = nums[0]
            for i in range(2, len(nums)+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            return dp[-1]

        if len(nums)== 1:
            return nums[0]
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))
        
