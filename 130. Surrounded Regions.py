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
