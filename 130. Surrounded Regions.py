'''
Problem:

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

'''



# Solution 1: using visited

from collections import deque
class Solution:

    def surroundedRegions(self, board):
            
        def canExplore(x, y, board):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "O"
            
            
        def findSurround(x,y, board):
            
            xDir = [0,1,0,-1]
            yDir = [1,0,-1,0]
            visited = [[False]*(len(board[0])) for _ in range(len(board))]
            
            q = deque()
            q.append([x,y])
            board[x][y] = "#"
            visited[x][y] = True
           
            while len(q):
                pos = q.popleft()
                x, y = pos[0],pos[1]
                for i in range(4):
                    xNew = x + xDir[i]
                    yNew = y + yDir[i]
                    # remember sanity check before put it in the queue!
                    if canExplore(xNew, yNew, board) and not visited[xNew][yNew]:
                        board[xNew][yNew] = "#"
                        visited[xNew][yNew] = True
                        q.append([xNew,yNew])
            return
   

        if not board or len(board) == 0 or len(board[0]) == 0:
            return
       
        row,col = len(board),len(board[0])
       
        # explore from the 4 boundries place
        for i in range(0, row):
            if board[i][0] == "O":
                findSurround(i, 0, board)
            if board[i][col-1] == "O":
                findSurround(i, col-1, board)
   
        for j in range(0, col):
            if board[0][j] == "O":           
                findSurround(0, j, board)
            if board[row-1][j] == "O":
                findSurround(row-1, j, board)
       
        # after the exploration
        # flip "O" to "X"
        # change "#" (expanded from boundry) back to "O"
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return





# Solution 2: not using visited

from collections import deque
class Solution(object):
    def solve(self, board):
            
        def canExplore(x, y, board):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "O"
            
            
        def findSurround(x,y, board):
            if not canExplore(x, y, board):
                return
            
            xDir = [0,1,0,-1]
            yDir = [1,0,-1,0]

            q = deque()
            q.append([x,y])
            board[x][y] = "#"
           
            while len(q):
                pos = q.popleft()
                x, y = pos[0],pos[1]
                for i in range(4):
                    xNew = x + xDir[i]
                    yNew = y + yDir[i]
                    # remember sanity check before put it in the queue!
                    if canExplore(xNew, yNew, board):
                        board[xNew][yNew] = "#"
                        q.append([xNew,yNew])
            return
   

        if not board or len(board) == 0 or len(board[0]) == 0:
            return
       
        row,col = len(board),len(board[0])
       
        # explore from the 4 boundries place
        for i in range(0, row):
            findSurround(i, 0, board)
            findSurround(i, col-1, board)
   
        for j in range(0, col):
            findSurround(0, j, board)
            findSurround(row-1, j, board)
       
        # after the exploration
        # flip "O" to "X"
        # change "#" (expanded from boundry) back to "O"
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return
