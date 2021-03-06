'''
Problem:

There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

'''

# Solution 1
# f[x] 现在还剩x个硬币,现在先手取硬币的人最后最多取硬币价值
# dp[i] = max(min(dp[i-2],dp[i-3])+values[n-i], min(dp[i-3],dp[i-4])+values[n-i]+values[n-i+1])

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):

        n = len(values)
        if n<3: return True
        
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = values[n-1]
        dp[2] = values[n-2]+values[n-1]
        dp[3] = values[n-3]+values[n-2]
        
        for i in xrange(4,n+1):
            dp[i] = max(min(dp[i-2],dp[i-3])+values[n-i], min(dp[i-3],dp[i-4])+values[n-i]+values[n-i+1])
        return dp[n]>sum(values)/2
        
        
        
        
        
# Solution 2
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):

        n = len(values)
        if n<3: return True
        
        sumVals = [0] * n
        sumVals[n-1] = values[n-1]
        for i in range(n-2,-1,-1):
            sumVals[i] = sumVals[i+1] + values[i]
        
        dp = [sumVals[n-1],sumVals[n-2]]
        
        for i in xrange(n-3, -1, -1):
            dp.append(max(values[i]+(sumVals[i+1]-dp[(n-1)-(i+1)]), values[i]+values[i+1]+(sumVals[i+2]-dp[(n-1)-(i+2)])))
        return dp[n-1] > sumVals[0]/2
