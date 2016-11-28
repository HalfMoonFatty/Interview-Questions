'''
Problem:

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''


# Solution 1: Math Combinatorial
# choose m-1 columns and n-1 rows from (m+n-2)

class Solution(object):
    def uniquePaths(self, m, n):
        if n == 1 or m == 1: return 1
        else: return math.factorial(m+n-2)/(math.factorial(n-1)*math.factorial(m-1))




# Solution 2-1: Back-Tracking

class Solution(object):
    def uniquePaths(self, m, n):

        def backTrack(r,c,m,n):
            if r == m-1 or c == n-1:
                return 1
            else:
                return backTrack(r+1,c,m,n) + backTrack(r,c+1,m,n)
        return backTrack(0,0,m,n)




# Solution 2-2: Back-Tracking + Memorization

class Solution(object):
    def uniquePaths(self, m, n):

        def backTrack(r,c,m,n,matrix):
            if r == m-1 or c == n-1:
                return 1

            if matrix[r+1][c] == -1:
                matrix[r+1][c] = backTrack(r+1,c,m,n,matrix)
            if matrix[r][c+1] == -1:
                matrix[r][c+1] = backTrack(r,c+1,m,n,matrix)
            matrix[r][c] = matrix[r+1][c] + matrix[r][c+1]
            return  matrix[r][c]

        matrix = [[-1 for i in range (n)] for j in range (m)]
        return backTrack(0,0,m,n,matrix)




# Solution 4: DP (Top-Down)
# T[i][j] means: the number of path from [0][0] to [i][j].

class Solution(object):
    def uniquePaths(self, m, n):
        
        dp = [[0]*(n+1) for _ in range (m+1)]
        dp[1][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if not (i == 1 and j == 1):    # note: do not overwrite start point
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] 

        return dp[-1][-1]
