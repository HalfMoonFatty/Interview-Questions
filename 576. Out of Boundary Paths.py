'''
Problem:

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:



Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:



Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
'''

'''
Solution: DP

数组dp[t][x][y]表示第t次移动时，坐标x, y处的移动路径总数。

状态转移方程：

dp[t + 1][x + dx][y + dy] += dp[t][x][y] 其中t表示移动的次数，dx, dy 取值 (1,0), (-1,0), (0,1), (0,-1)

当x + dx或者y + dy超出边界时，将结果累加至最终答案。

'''



class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
        dp = [[[0] *n for x in range(m)] for t in range(N+1)]    # dp[t][x][y]
        dp[0][i][j] = 1
        ans = 0
        for t in range(N):
            for x in range(m):
                for y in range(n):
                    for dx, dy in dz:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            dp[t+1][nx][ny] = (dp[t+1][nx][ny] + dp[t][x][y]) % MOD
                        else:
                            ans = (ans + dp[t][x][y]) % MOD
        return ans
        
        
        
        
        
# Optimize Space Complexity:

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
        dp = [[0] *n for x in range(m)]
        dp[i][j] = 1
        ans = 0
        for t in range(N):
            ndp = [[0] *n for x in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx, dy in dz:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            ndp[nx][ny] = (ndp[nx][ny] + dp[x][y]) % MOD
                        else:
                            ans = (ans + dp[x][y]) % MOD
            dp = ndp
        return ans
        
