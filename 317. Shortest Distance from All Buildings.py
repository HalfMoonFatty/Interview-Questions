'''
Problem:

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. 
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

'''

'''
Note:

局部变量
	cur_dist: 从每一个建筑出发，新建一张图记录每一块地到当前建筑的距离. 基本的 shortest distance problem。
	
全局变量
	total_dist：所有cur_dist的叠加。例如本例中，有三张cur_dist.
	reach: 每块地，被每一个建筑遍历都+1, 也就是每块地能被多少建筑遍历。最后只有能被全部建筑遍历的地，才能参选。
	numBuilding
'''


from collections import deque
import sys

class Solution(object):
    def shortestDistance(self, grid):
        
        def canExplore(nx, ny):
            return nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 0

        def bfs_dist(i,j):

            xdir = [0,1,0,-1]
            ydir = [1,0,-1,0]
            visited = [[False for _ in range(n)] for _ in range(m)]
            cur_dist = [[0 for _ in range(n)] for _ in range(m)]

            q = deque()
            q.append([i,j])
            while len(q):
                x,y = q.popleft()
                total_dist[x][y] += cur_dist[x][y]  # accumulate total_dist[x][y]

                for d in range(4):
                    nx = x + xdir[d]
                    ny = y + ydir[d]
                    if canExplore(nx, ny) and not visited[nx][ny]:
                        cur_dist[nx][ny] = cur_dist[x][y] +1
                        reach[nx][ny] += 1	# count reached by how many buidling for each [x][y]
                        visited[nx][ny] = True
                        q.append([nx,ny])
            return



        m,n = len(grid),len(grid[0])
        reach = [[0 for j in range(n)] for i in range(m)]
        total_dist = [[0 for j in range(n)] for i in range(m)]
        numBuilding = 0
       
        # for each building calculte shortest distance to every empty land
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:   
                    numBuilding += 1
                    bfs_dist(i,j)


        shortest = sys.maxint
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == numBuilding:
                    shortest = min(shortest, total_dist[i][j])
        return shortest if shortest < sys.maxint else -1
