'''
Problem:

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
nums = [
[9,9,4],
[6,6,8],
[2,1,1]
]
Return 4; The longest increasing path is [1, 2, 6, 9].

Example 2:
nums = [
[3,4,5],
[3,2,6],
[2,2,1]
]
Return 4; The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def canExplore(nx,ny,x,y):
            return 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny] > matrix[x][y] 
            
        def dfs(x,y,cache):
            if cache[x][y] > 0:
                return cache[x][y]
            
            localMaxPath = 1
            xDir = [1,0,-1,0]
            yDir = [0,1,0,-1]
            for d in range(4):
                nx,ny = x+xDir[d], y+yDir[d]
                if canExplore(nx,ny,x,y):
                    localMaxPath = max(localMaxPath, 1+dfs(nx,ny,cache))
            cache[x][y] = localMaxPath
            return localMaxPath
        
        
        
        if not matrix: return 0
    
        m,n = len(matrix), len(matrix[0])
        cache = [[0]*n for _ in range(m)]
        globalMaxPath = 0
        
        for i in range(m):
            for j in range(n):
                globalMaxPath = max(globalMaxPath,dfs(i,j,cache))
        return globalMaxPath
            
        
