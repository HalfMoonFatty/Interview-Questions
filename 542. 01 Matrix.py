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

Similar Problem: 286. Walls and Gates


Time complexity: O(r⋅c).
Since, the new cells are added to the queue only if their current distance is greater than the calculated distance, cells are not likely to be added multiple times.

Space complexity: O(r⋅c). Additional O(r⋅c) for queue.

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
                    
                

            
'''
Solution 2: Calculate the distance from each '1' to its nearest '0'. This method got TLE.

Similar Problem: 317. Shortest Distance from All Buildings
'''

import collections
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def getDistance(i, j, matrix):
            visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
            visited[i][j] = True
            
            q = collections.deque()
            q.append((i,j))
            
            xDir = (0,1,0,-1)
            yDir = (1,0,-1,0)
            step = 0
            while len(q):
                step += 1
                qsize = len(q)
                for _ in range(qsize):
                    x,y = q.popleft()
                    for d in range(4):
                        nx,ny = x+xDir[d], y+yDir[d]
                        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and not visited[nx][ny]:
                            if matrix[nx][ny] == 0:
                                result[i][j] = step
                                return
                            visited[nx][ny] = True
                            q.append((nx,ny))

            return

        
        result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    getDistance(i,j,matrix)
                    
            
        return result
                    
                
