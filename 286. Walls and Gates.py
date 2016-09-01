'''
Problem:

You are given a m x n 2D grid initialized with these three possible values.

1. -1 - A wall or an obstacle.
2. 0 - A gate.
3. INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
0    -1 INF INF

After running your function, the 2D grid should be:
3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4

'''

from collections import deque
import sys
class Solution(object):
    def wallsAndGates(self, rooms):
        """
            :type rooms: List[List[int]]
            :rtype: void Do not return anything, modify rooms in-place instead.
            """
        def canExplore(x, y, rooms):
            return 0<=x<len(rooms) and 0<=y<len(rooms[0]) and rooms[x][y] != -1
       

        def findDist(room, q):
            xDir = [0,-1, 0, 1]
            yDir = [-1,0, 1, 0]
           
            while len(q):
                pos = q.popleft()
                x, y = pos[0], pos[1]
               
                for i in range(4):
                    xNew = x + xDir[i]
                    yNew = y + yDir[i]
                    # if cannot explore or already been updated, skip it:
                    if canExplore(xNew, yNew, rooms) and rooms[xNew][yNew] == sys.maxint:
                        rooms[xNew][yNew] = rooms[x][y]+1
                        q.append([xNew,yNew])
       
            return
       
       
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return

        row,col = len(rooms),len(rooms[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append([i,j])
        findDist(rooms,q)
        return
