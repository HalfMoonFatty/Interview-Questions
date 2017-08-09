'''
Problem:

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3

'''


# Solution 1: Union Find



class Solution(object):
    def numIslands(self, grid):

        def findRoot(x):
            if x == unionSet[x]:
                return x
            unionSet[x] = findRoot(unionSet[x])
            return unionSet[x]
            
        def union(set1,set2):
            rootX = findRoot(set1)
            rootY = findRoot(set2)
            unionSet[rootX] = rootY
            return
       
       
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
       
        h,w = len(grid),len(grid[0])
        unionSet = [i for i in range(h*w)]    # initially every position is a union of itself
        count = 0
        xDir = [0,1,0,-1]
        yDir = [1,0,-1,0]
       
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    curSet = i*w+j
                    count += 1
                    for p in range(4):
                        x = i + xDir[p]
                        y = j + yDir[p]
                        neighbourSet = x*w+y
                        if 0<=x<h and 0<=y<w and grid[x][y] == "1":
                            if findRoot(curSet) != findRoot(neighbourSet): 
                                count -= 1
                                union(curSet,neighbourSet)
        return count




# Solution 1: DFS explore function is the ONLY difference with BFS function


class Solution(object):
    def numIslands(self, grid):

        def explore(x, y, grid, visited):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1 or grid[x][y] == "0" or visited[x][y] == True:
                return
            else:
                visited[x][y] = True
                explore(x, y-1, grid, visited)
                explore(x+1, y, grid, visited)
                explore(x-1, y, grid, visited)
                explore(x, y+1, grid, visited)
            return
   

        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
   
        numIsland = 0
        row,col = len(grid),len(grid[0])
        visited = [[False for t in range(col)] for s in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] != "0" and not visited[i][j]:
                    explore(i, j, grid, visited)
                    numIsland += 1

    	return numIsland





'''
Solution 2: BFS
Tricky: need to mark every postion as visited BEFORE we put them into the Queue. 
I tried to mark a postition when we poll it out from the queue, but this case we put a lot of wasted postions in the queue. 
'''

from collections import deque
class Solution(object):
    def numIslands(self, grid):

        def canExplore(x, y, grid, visited):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and not visited[x][y]


        def explore(x, y, grid, visited):
            if canExplore(x, y, grid, visited):
                xdir = [0,1,0,-1]
                ydir = [1,0,-1,0]
                
                q = deque()
                q.append([x,y])
                while len(q):
                    x,y = q.popleft()
                    #visited[x][y] = True   # TLE
                    for i in range(4):
                        nx,ny = x+xdir[i], y+ydir[i]
                        if canExplore(nx,ny, grid, visited):
                            q.append([nx,ny])
                            visited[nx][ny] = True

   
   
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
       
        numIsland = 0
        row,col = len(grid),len(grid[0])
        visited = [[False for t in range(col)] for s in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] != "0" and not visited[i][j]:
                    explore(i, j, grid, visited)
                    numIsland += 1

        return numIsland



