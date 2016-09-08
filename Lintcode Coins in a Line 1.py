'''
Problem:
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. 
The player who take the last coin wins.

Could you please decide the first play will win or lose?
'''

# Normal DP solution:
class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        if n == 1 or n == 2 or n == 4: return True
        if n == 0 or n == 3: return False
        
        dp = [False] * (n+1)
        dp[1] = True
        dp[2] = True
        dp[3] = False
        dp[4] = True
        for i in range(5,n+1):
            dp[i] = (dp[i-2] and dp[i-3]) or (dp[i-3] and dp[i-4])
            
        return dp[-1]
    
    
# Math
class Solution:
    def firstWillWin(self, n):
        if n%3==0: return False
        else: return True
