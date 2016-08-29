'''
Problem:

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# dp[x] = dp[x - 1] + dp[x - 2]

class Solution:

    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]

'''
Solution2: Space O(1)：
'''
class Solution:
    def climbStairs(self, n):
        a = b = 1
        for x in range(2, n + 1):
            a, b = b, a + b
        return b
