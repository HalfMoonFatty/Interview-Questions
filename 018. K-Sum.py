'''
Problem:

Given n distinct positive integers, integer k (k <= n) and a number target.
Find k numbers where sum is target. Calculate how many solutions there are?

Example
Given [1,2,3,4], k = 2, target = 5.
There are 2 solutions: [1,4] and [2,3].
Return 2.
'''

'''
Solution: DP

dp[i][j][t] 表示从前i个数中，挑出j个数，组成和为t有多少种方法。

转移方程：
dp[i][j][t] = dp[i-1][j][t]
if t - A[i-1] >= 0:
    dp[i][j][t] += dp[i-1][j-1][t-A[i-1]]
    
(1) 可以把当前A[i - 1]这个值包括进来，所以需要加上dp[i - 1][j - 1][t - A[i - 1]]（前提是t - A[i - 1]要大于0）
(2) 可以不选择A[i - 1]这个值，这种情况就是dp[i - 1][j][t]，也就是说直接在前i-1个值里选择一些值加到target.
'''


class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        if target < 0: return 0
        
        dp = [[[0] * (target+1) for j in range(k+1) ] for i in range(len(A)+1)]
        for i in range(len(A)+1):
            for j in range(k+1):
                for t in range(target+1):
                    if j == t == 0: # corner
                        dp[i][j][t] = 1
                    elif not (i == 0 or j == 0 or t == 0):   # do not modify edges
                        dp[i][j][t] = dp[i-1][j][t]
                        if t - A[i-1] >= 0:
                            dp[i][j][t] += dp[i-1][j-1][t-A[i-1]]
        return dp[-1][-1][-1]
