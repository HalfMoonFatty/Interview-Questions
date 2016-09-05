'''
Problem:

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note:
     You may assume that n is not less than 2.

Hint:
There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

'''
class Solution(object):
    def integerBreak(self, n):
        """
            :type n: int
            :rtype: int
            """
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(j,dp[j])*(max(i-j, dp[i-j])))
        return dp[-1]
        
        
# Math solution

class Solution(object):
    def integerBreak(self, n):

        return 1 if n <= 2
        return 2 if n == 3
        return 4 if n == 4

        dp = [0] * (n+1)
        dp[2],dp[3], dp[4]= 2,3,4

        for i in range(5,n+1):
            dp[i] = 3 * dp[i-3]
        return dp[-1]
