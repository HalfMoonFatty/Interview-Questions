from collections import deque
import sys

class Solution(object):
    def shortestDistance(self, grid):
        
        def bfs_dist(i,j):
            xdir = [0,1,0,-1]
            ydir = [1,0,-1,0]
            visited = [[False for yy in range(n)] for xx in range(m)]   # shadow var don't use i and j

            q = deque()
            q.append([i,j])
            level = 1
           
            while len(q):
                size = len(q)
                for _ in range(size):   # note we only update items at the "same level" in the queue
                    cur = q.popleft()
                    for d in range(4):
                        x = cur[0] + xdir[d]
                        y = cur[1] + ydir[d]
                        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 0 and not visited[x][y]:
                            distance[x][y] += level
                            reach[x][y] += 1
                            visited[x][y] = True
                            q.append([x,y])
       
                level += 1  # note hop added after finish "size" items in the queue
            return


        m,n = len(grid),len(grid[0])
        reach = [[0 for j in range(n)] for i in range(m)]
        distance = [[0 for j in range(n)] for i in range(m)]
        numBuilding = 0
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:   # for each building
                    numBuilding += 1
                    bfs_dist(i,j)


        shortest = sys.maxint
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == numBuilding:
                    shortest = min(shortest, distance[i][j])
        return shortest if shortest < sys.maxint else -1


s = Solution()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print s.shortestDistance(grid)





# buggy
from collections import deque
import sys

class Solution(object):
    def shortestDistance(self, grid):
        def canExplore(nx, ny):
            return nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 0

        def bfs_dist(i,j):
            xdir = [0,1,0,-1]
            ydir = [1,0,-1,0]
            visited = [[False for yy in range(n)] for xx in range(m)]   # shadow var don't use i and j

            q = deque()
            q.append([i,j])
            level = 1
           
            while len(q):
                cur = q.popleft()
                x,y = cur[0],cur[1]

                for d in range(4):
                    nx = x + xdir[d]
                    ny = y + ydir[d]
                    if canExplore(nx, ny) and not visited[nx][ny]:
                        distance[nx][ny] = distance[x][y] +1
                        reach[x][y] =  reach[x][y] + 1
                        visited[nx][ny] = True
                        q.append([nx,ny])
            return


        m,n = len(grid),len(grid[0])
        reach = [[0 for j in range(n)] for i in range(m)]
        distance = [[0 for j in range(n)] for i in range(m)]
        numBuilding = 0
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:   # for each building
                    numBuilding += 1
                    bfs_dist(i,j)


        shortest = sys.maxint
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == numBuilding:
                    shortest = min(shortest, distance[i][j])
        return shortest if shortest < sys.maxint else -1


s = Solution()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print s.shortestDistance(grid)
