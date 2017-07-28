'''
Problem:

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means wall and 0 means empty space. You may assume that the borders of the maze are walls. 
The start and destination coordinates are represented by row and column indexes.



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
Solution 1: BFS

In this case, we try to explore the search space on a level by level basis. i.e. We try to move in all the directions at every step. 
When all the directions have been explored and we still don't reach the destination, then only we proceed to the new set of traversals from the new positions obtained.

In order to implement this, we make use of a queue. We start with the ball at the start position. 
For every current position, we add all the new positions possible by traversing in all the four directions(till reaching the wall or boundary) 
into the queue to act as the new start positions and mark these positions as True in the visited array. When all the directions have been covered up, 
we remove a position value, s, from the front of the queue and again continue the same process with s acting as the new start position.

Further, in order to choose the direction of travel, we make use of a dir array, which contains 4 entries. 
Each entry represents a one-dimensional direction of travel. To travel in a particular direction, we keep on adding the particular entry of the dirs array 
till we hit a wall or a boundary. For a particular start position, we do this process of dir addition for all all the four directions possible.

If we hit the destination position at any moment, we return a True directly indicating that the destination position can be reached starting from the start position.


Time complexity : O(mn). Complete traversal of maze will be done in the worst case. Here, m and n refers to the number of rows and coloumns of the maze.
Space complexity : O(mn). visited array of size m∗n is used and queue size can grow upto m∗n in worst case.
'''

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m,n = len(maze), len(maze[0])

        xDir = [0,1,0,-1]
        yDir = [1,0,-1,0]
        visited = [[False] * n for _ in range(m)]
        q = collections.deque([start])
        
        visited[start[0]][start[1]] = True
        while len(q):
            cur = q.popleft()
            if cur == destination:
                return True
            for i in range(4):
                nx, ny = cur[0]+xDir[i], cur[1]+yDir[i]
                # rolling till meet wall
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += xDir[i]
                    ny += yDir[i]
                if not visited[nx-xDir[i]][ny-yDir[i]]:
                    q.append([nx-xDir[i],ny-yDir[i]])
                    visited[nx-xDir[i]][ny-yDir[i]] = True  # visited
        return False
        


'''
Solution 2: DFS


In order to do this traversal, one of the simplest schemes is to undergo depth first search. 
In this case, we choose one path at a time and try to go as deep as possible into the levels of the tree before going for the next path. 
In order to implement this, we make use of a recursive function dfs(maze, start, desination, visited). This function takes the given 
maze array, the start position and the destination position as its arguments along with a visited array. 
A True value at visited[i][j] represents that the current position has already been reached earlier during the path traversal. 
We make use of this array so as to keep track of the same paths being repeated over and over. 
We mark a True at the current position in the visited array once we reach that particular positon in the maze.


From every start position, we can move continuously in either left, right, upward or downward direction till we reach the boundary or a wall. 
Thus, from the start position, we determine all the end points which can be reached by choosing the four directions. For each of the cases, 
the new endpoint will now act as the new start point for the traversals. The destination, obviously remains unchanged. 
Thus, now we call the same function four times for the four directions, each time with a new start point obtained previously.

If any of the function call returns a True value, it means we can reach the desination.

Time complexity : O(mn). 
Space complexity : O(mn). visited array of size m∗n is used.

'''

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def dfs(maze, cur, destination, visited):
            if visited[cur[0]][cur[1]]: 
                return False
            if cur == destination: 
                return True
            
            visited[cur[0]][cur[1]] = True    # visited
            for i in range(4):
                nx, ny = cur[0]+xDir[i], cur[1]+yDir[i]
                # rolling till meet wall
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += xDir[i]
                    ny += yDir[i]
                if dfs(maze, [nx-xDir[i], ny-yDir[i]], destination, visited):
                    return True
                       
            return False
                       
                       
        m,n = len(maze), len(maze[0])
        xDir = [0,1,0,-1]
        yDir = [1,0,-1,0]
        visited = [[False] * n for _ in range(m)]
        return dfs(maze, start, destination, visited)
        
        
                
