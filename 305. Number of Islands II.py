'''
Problem:

A 2d grid map of m rows and n columns is initially filled with water. 
We may perform an addLand operation which turns the water at position (row, col) into a land. 
Given a list of positions to operate, count the number of islands after each addLand operation. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]


Challenge：
     Can you do it in time complexity O(k log mn), where k is the length of the positions? 

'''




'''
Solution: Union Find

本题与第一问不同的地方在于，本题是不能access 整个grid的，而且positions 也是依序一个一个给出的，于是需要一个全局的记录知道一个点是不是Island。
本题的巧妙之处就在于：一上来先把 UnionSet全部设为 "-1" 来表示每一个position 都是water 不能做island的union动作。

然后对于position中的每一个点（一定为“1”,看题）：
    先把Unionset 更新，把该点mark为已经是island了。
    遍历current position周围的4个点:
    如果不是水（unionSet[neighbourSet] != -1）而且跟当前的岛是两个Union的话，就跟当前点做Union,注意合成一个island后要count -1
'''


class Solution(object):
   
    def numIslands2(self, m, n, positions):
        """
            :type m: int
            :type n: int
            :type positions: List[List[int]]
            :rtype: List[int]
            """
            
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
       

        unionSet = [-1 for i in range(m*n)]         # init every pos as water (cannot union)
        result = []
        xDir = [0,1,0,-1]
        yDir = [1,0,-1,0]
       
        for pos in positions:     
            if result: count = result[-1]+1         # count up base on the last previous results
            else: count = 1
           
            curSet = pos[0]*n+pos[1]                # position to unionSet index 
            unionSet[curSet] = curSet              
            for p in range(4):                
                x = pos[0] + xDir[p]
                y = pos[1] + yDir[p]
                neighbourSet = x*n+y                # position to unionSet index 
                if 0<=x<m and 0<=y<n and unionSet[neighbourSet] != -1:    # not water
                    if findRoot(curSet) != findRoot(neighbourSet):
                        count -= 1
                        union(curSet,neighbourSet)
            result.append(count)
       
        return result




