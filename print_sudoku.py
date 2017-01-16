'''
Problem:
    Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Note:
    A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

# rowInd = 3* (i/3) + j/3  
# colInd = 3* (i%3) + j%3


class Solution(object):
    def isValidSudoku(self, board):
        
        for i in range(9):
            row = set()
            col = set()
            block = set()
            
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                row.add(board[i][j])

                if board[j][i] != '.' and board[j][i] in col:
                    return False
                col.add(board[j][i])

                rowInd = 3* (i/3) + j/3  
                colInd = 3* (i%3) + j%3

                if board[rowInd][colInd] != '.' and board[rowInd][colInd] in block:
                    return False
                block.add(board[rowInd][colInd])

        return True



'''
Problem:
    Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.'.
    You may assume that there will be only one unique solution.
'''

class Solution(object):

    def solveSudoku(self, board):

        def isValidSudoku(row, col, board, c):
            if int(c) not in range(1,10):
                return False
                
            for i in range(9):
                if board[row][i] != '.' and int(board[row][i]) == int(c) and i != col:
                    return False
                if board[i][col] != '.' and int(board[i][col]) == int(c) and i != row:
                    return False

            rbase = row/3*3
            cbase = col/3*3
            for i in range(rbase,rbase+3):
                for j in range(cbase,cbase+3):
                    if board[i][j] != '.' and int(board[i][j]) == int(c) and (i, j)!=(row, col):
                        return False
            return True


        def canSolve(row, col, board):
            if row == 9:
                return True
            
            if col == 8:    # next row
                nextRow = row+1
                nextCol = 0
                
            else:    # next column
                nextRow = row
                nextCol = col+1

            if board[row][col] != '.':
                return canSolve(nextRow, nextCol, board)

            else:
                for n in range(1,10):  # choose a number from 1 to 9
                    if isValidSudoku(row, col, board, n):
                        board[row][col] = str(n)
                        if canSolve(nextRow, nextCol, board):
                            return True
                        board[row][col] = '.'
                return False


        if len(board) < 9 or len(board[0]) < 9:
            return
        canSolve(0,0,board)
        return