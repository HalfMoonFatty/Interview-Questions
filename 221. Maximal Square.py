'''
Problem:

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0

        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        maxLen = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1': # string '1' not int
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    maxLen = max(maxLen,dp[i][j])
        return maxLen * maxLen
