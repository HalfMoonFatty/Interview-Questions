'''
Problem:

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1: 
Input:
0 0 0
0 1 0
0 0 0

Output:
0 0 0
0 1 0
0 0 0


Example 2: 
Input:
0 0 0
0 1 0
1 1 1

Output:
0 0 0
0 1 0
1 2 1


Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

'''
Solution 1: Do a BFS on multiple sources - matrix[i][j] == 0

'''

import collections
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        
        q = collections.deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i,j))
                    result[i][j] = 0
            
            
        xDir = (0,1,0,-1)
        yDir = (1,0,-1,0)
        while len(q):
            x, y = q.popleft()
            for d in range(4):
                nx,ny = x+xDir[d], y+yDir[d]
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    q.append((nx,ny))

        return result
                    
                
