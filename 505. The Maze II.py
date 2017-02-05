'''
Problem:


There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. 
The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving shortest distance in the maze. 
The distance is defined by the number of empty spaces the ball go through from the start position (exclude) to the hole (include). 
Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there may have several different shortest ways, 
you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The ball and hole coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"
Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".


Example 2

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)
Output: "impossible"
Explanation: The ball cannot reach the hole.


Note:
There are only one ball and one hole in the maze.
The ball and hole will only exist in the empty space, and they will not at the same position initially.
The given maze doesn't contain border (like the red rectangle in the example pictures), but you should assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the length and width of the maze won't exceed 30.

'''



'''
Solution 1：预处理 + 单源最短路

首先预处理迷宫maze中各点坐标向四个方向运动最终可以达到的坐标，用数组 destmap (destination) 记录。

例如dmap[(3, 2)]['u']表示从坐标(3, 2)出发向上运动最终可以到达的位置。

利用数组ballmap记录迷宫中各点坐标到小球初始位置的最短距离dist与最短路径path。

维护队列queue，初始将(ball, 0, '')加入queue（坐标，距离，路径）

记当前坐标为p，从p出发，分别向u, d, l, r四个方向扩展并更新下一个坐标np的最短距离与路径，保存在ballmap中。

如果np得到更新，则将np加入队列；重复此过程直到queue为空

返回ballmap[hole]
'''

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        def distance(pa, pb):
            return abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
            
        w, h = len(maze), len(maze[0])
        ball, hole = tuple(ball), tuple(hole)
        # pre-processing destination map
        destmap = collections.defaultdict(lambda: collections.defaultdict(int))
        for dir in 'dlru': destmap[hole][dir] = hole
        for x in range(w):
            for y in range(h):
                if maze[x][y] or (x, y) == hole: continue
                destmap[(x, y)]['u'] = destmap[(x - 1, y)]['u'] if x > 0 and destmap[(x - 1, y)]['u'] else (x, y)
                destmap[(x, y)]['l'] = destmap[(x, y - 1)]['l'] if y > 0 and destmap[(x, y - 1)]['l'] else (x, y)
        for x in range(w - 1, -1, -1):
            for y in range(h - 1, -1, -1):
                if maze[x][y] or (x, y) == hole: continue
                destmap[(x, y)]['d'] = destmap[(x + 1, y)]['d'] if x < w - 1 and destmap[(x + 1, y)]['d'] else (x, y)
                destmap[(x, y)]['r'] = destmap[(x, y + 1)]['r'] if y < h - 1 and destmap[(x, y + 1)]['r'] else (x, y)
                
        ballmap = {ball : (0, '')}
        queue = collections.deque([(ball, 0, '')])
        while queue:
            pos, dist, path = queue.popleft()
            for dir in 'dlru':
                if dir not in destmap[pos]: continue
                npos = destmap[pos][dir]
                ndist = dist + distance(pos, npos)
                npath = path + dir
                if np not in ballmap or (ndist, npath) < ballmap[npos]:
                    ballmap[npos] = (ndist, npath)
                    queue.append((npos, ndist, npath))
        return ballmap[hole][1] if hole in ballmap else 'impossible'
        
        
        

'''
Solution 2：预处理 + Dijkstra算法
'''

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        def distance(pa, pb):
            return abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
            
        w, h = len(maze), len(maze[0])
        ball, hole = tuple(ball), tuple(hole)
        # pre-processing destination map
        destmap = collections.defaultdict(lambda: collections.defaultdict(int))
        for dir in 'dlru': destmap[hole][dir] = hole
        for x in range(w):
            for y in range(h):
                if maze[x][y] or (x, y) == hole: continue
                destmap[(x, y)]['u'] = destmap[(x - 1, y)]['u'] if x > 0 and destmap[(x - 1, y)]['u'] else (x, y)
                destmap[(x, y)]['l'] = destmap[(x, y - 1)]['l'] if y > 0 and destmap[(x, y - 1)]['l'] else (x, y)
        for x in range(w - 1, -1, -1):
            for y in range(h - 1, -1, -1):
                if maze[x][y] or (x, y) == hole: continue
                destmap[(x, y)]['d'] = destmap[(x + 1, y)]['d'] if x < w - 1 and destmap[(x + 1, y)]['d'] else (x, y)
                destmap[(x, y)]['r'] = destmap[(x, y + 1)]['r'] if y < h - 1 and destmap[(x, y + 1)]['r'] else (x, y)
                
        ballmap = {ball : (0, '', ball)}
        visited = set()
        while ballmap:
            dist, path, pos = min(ballmap.values())
            if pos == hole: return path   # find a vlid path
            del bmap[pos]
            visited.add(pos)
            for dir in 'dlru':
                if dir not in dmap[pos]: continue
                npos = dmap[pos][dir]
                ndist = dist + distance(pos, npos)
                npath = path + dir
                if np not in visited and (npos not in ballmap or (ndist, npath, npos) < bmap[npos]):
                    bmap[npos] = (ndist, npath, npos)
        return 'impossible'
