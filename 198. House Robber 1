'''
Problem:

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''

'''
dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。
状态转移方程： dp[i] = max(dp[i-1], dp[i-2] + num[i-1])
Time O(n)  SpaceO(n)
'''

class Solution(object):
    def rob(self, nums):

        size = len(nums)
        dp = [0] * (size +1)
        if size:
            dp[1] = nums[0]
        for i in range(2, size +1):
            dp[i] = max(dp[i -1], dp[i -2] + nums[i -1])
        return dp[size]
