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





'''
Solution 1: DFS

numsIslands function:
    - Scan the entire grid O(n^2)
        - if this position is visited or is water, then go to the next position
        - else call "explore" function to explore positions around the current position
        - after explore all surrounded regions, add one(one more island explored)

explore function(DFS) This function is the ONLY difference with BFS function
    - call "canExplore" for boundry check and screen out already visited positions
    - then call explore on 4 directiions (4 neighbours) one by one
   
canExplore function:
    - for boundry check and screening for visited positions
    - during interview, if you cannot finish this function, the interviewer will understand.
   

Reference: Solution without extra space of visited -- Directly mark visited place as "x" or "0"
https://leetcode.com/discuss/31011/simple-java-solution
'''

class Solution(object):
    def numIslands(self, grid):
        """
            :type grid: List[List[str]]
            :rtype: int
            """
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
        row = len(grid)
        col = len(grid[0])
        visited = [[False for t in range(col)] for s in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0" or visited[i][j]:
                    continue
                else:
                    explore(i, j, grid, visited)
                    numIsland += 1

    	return numIsland





'''
Solution 2: BFS

explore function (BFS) This function is the ONLY difference with DFS function
    - call "canExplore" for boundry check and screen out already visited positions
    - Queue is your best friend when coming to BFS:
        - get one postions
        - then put all of its neighbour of this position "one-by-one"
        - the tricky thing here is that we need to mark every postion as visited BEFORE we put them into the Queue. 
        I tried to mark a postition when we poll it out from the queue, but this case we put a lot of wasted postions in the queue. 
        Hmmm, very tricky.
'''

import Queue
class Solution(object):
    def numIslands(self, grid):

        def canExplore(x, y, grid, visited):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and visited[x][y] == False:
                return True
            else:
                return False
       
        def explore(x, y, grid, visited):
            if not canExplore(x, y, grid, visited):
                return
            else:
                q = Queue.Queue() # Queue initialization
                q.put([x,y])
               
                while not q.empty():
                    pos = q.get()
                    x,y = pos[0],pos[1]
                    # visited[x][y] = True   # keep
                   
                    if canExplore(x+1, y, grid, visited):
                        q.put([x+1,y])
                        visited[x+1][y] = True
                    if canExplore(x-1, y, grid, visited):
                        q.put([x-1,y])
                        visited[x-1][y] = True
                    if canExplore(x, y+1, grid, visited):
                        q.put([x,y+1])
                        visited[x][y+1] = True
                    if canExplore(x, y-1, grid, visited):
                        q.put([x,y-1])
                        visited[x][y-1] = True
            return
   
   
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
       
        numIsland = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False for t in range(col)] for s in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0" or visited[i][j]:
                    continue
                else:
                    explore(i, j, grid, visited)
                    numIsland += 1

    return numIsland




