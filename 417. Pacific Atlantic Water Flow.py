'''
Problem:

    Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
    the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

    Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

    Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

'''



from collections import deque
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def bfs(q, visited):
            xdir = (0,1,0,-1)
            ydir = (1,0,-1,0)
            while len(q):
                x,y = q.popleft()
                for d in range(4):
                    nx, ny = x+xdir[d], y+ydir[d]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] >= matrix[x][y]:
                        visited[nx][ny] = True
                        q.append([nx,ny])
            return
             
             
                        
        if not matrix: return []
        
        m,n = len(matrix), len(matrix[0])
        atlvisited = [[False]*n for _ in range(m)]
        pacvisited = [[False]*n for _ in range(m)]
        
        atlq = deque()
        pacq = deque()
        
        # init atlq and pacq
        for i in range(m):
            atlq.append([i,0])
            pacq.append([i,n-1])
            atlvisited[i][0] = True
            pacvisited[i][n-1] = True
        
        for j in range(n):
            atlq.append([0,j])
            pacq.append([m-1,j])
            atlvisited[0][j] = True
            pacvisited[m-1][j] = True
        
        bfs(atlq, atlvisited)
        bfs(pacq, pacvisited)
        
        # add the intersection to the result
        result = []
        for i in range(m):
            for j in range(n):
                if atlvisited[i][j] and pacvisited[i][j]:
                    result.append([i,j])
        return result
