'''
Problem:

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
     n and k are non-negative integers.
'''

# dp[i] =(dp[i-2]+dp[i-1])*(k-1)
class Solution(object):
    def numWays(self, n, k):

        if n == 0:
            return 0
        elif n == 1:
            return k

        dp = [0 for i in range(n)]
        dp[0] = k * 1
        dp[1] = k * (k-1)
        for i in range(2,n):
            dp[i] = (dp[i-2]+dp[i-1])*(k-1)
        return dp[-1]+dp[-2]
