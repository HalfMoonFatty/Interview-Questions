'''
Problem:

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
     n and k are non-negative integers.
'''

#if dp[i] paint diff color with dp[i-1]: dp[i] = dp[i-1]*(k-1)
#if dp[i] paint same color with dp[i-1]: 
    # then dp[i-1] must not paint the same with dp[i-2] (i.e. dp[i-1] is different color with dp[i-2] => dp[i-2]*(k-1)) 
    # dp[i] = dp[i-2]*(k-1)*1
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
