'''
Problem:

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, 
compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

'''



import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        
        heap = []
        m,n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        water = 0
        
        #add boundry into heap
        for j in range(n):
            heapq.heappush(heap,(heightMap[0][j],0,j))
            heapq.heappush(heap,(heightMap[-1][j],m-1,j))
            visited[0][j] = True
            visited[-1][j] = True
                
        for i in range(1,m-1):
            heapq.heappush(heap,(heightMap[i][0],i,0))
            heapq.heappush(heap,(heightMap[i][-1],i,n-1))
            visited[i][0] = True
            visited[i][-1] = True
            
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        while len(heap):
            cur = heapq.heappop(heap)
            for i in range(4):
                nx = cur[1]+dx[i]
                ny = cur[2]+dy[i]
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap,(max(cur[0],heightMap[nx][ny]),nx,ny))    # add the heighest to the heap
                    water += max(0, cur[0] - heightMap[nx][ny])
        return water
        
