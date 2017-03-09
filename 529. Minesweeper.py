'''
Problem:


Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 
'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') 
represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing 
this position according to the following rules:

- If a mine ('M') is revealed, then the game is over - change it to 'X'.
- If an empty square ('E') with NO adjacent mines, change it to blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
- If an empty square ('E') with at least one adjacent mine, change it to a digit ('1' to '8') representing the number of adjacent mines.
- Return the board when no more squares will be revealed.


Example 1:
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]


Example 2:
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]


Note:
The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
'''

# BFS

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def countMine(i,j):
            count = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni,nj = i+di, j+dj
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'M':
                        count += 1
            return str(count) if count else 'B'
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        q = collections.deque()
        q.append([x,y])
        
        board[x][y] = countMine(x, y)
        if board[x][y] != 'B':    # if not blank just change to digit and STOP 
            return board
        
        while len(q):
            i,j = q.popleft()
            board[i][j] = countMine(i,j)
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni,nj = i+di, j+dj
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                        if board[ni][nj] == 'E':
                            board[ni][nj] = countMine(ni, nj)
                            if board[ni][nj] == 'B':    # recursively reveal
                                q.append((ni, nj))
        return board
