'''
Problem:

    Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
    A valid Sudoku board (partially filled) is not necessarily solvable.
    Only the filled cells need to be validated.
'''



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
