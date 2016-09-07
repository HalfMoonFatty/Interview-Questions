'''
Problem:

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m,n = len(grid),len(grid[0])

        # init values for corner dp[0][0] and edges dp[0][c] and dp[r][0]
        dp = [[0 for c in range (n)] for r in range(m)]
        dp[0][0] = grid[0][0]
        for c in range(1,n):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1,m):
            dp[r][0] = dp[r-1][0] + grid[r][0]

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = min(dp[r-1][c] + grid[r][c], dp[r][c-1] + grid[r][c])
        return dp[m-1][n-1]
