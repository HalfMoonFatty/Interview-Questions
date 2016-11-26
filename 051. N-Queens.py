'''
Problem:

    The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
    
    Given an integer n, return all distinct solutions to the n-queens puzzle.

    Each solution contains a distinct board configuration of the n-queens' placement, 
    where 'Q' and '.' both indicate a queen and an empty space respectively.

For example, There exist two distinct solutions to the 4-queens puzzle:

[
[".Q..",  // Solution 1
"...Q",
"Q...",
"..Q."],

["..Q.",  // Solution 2
"Q...",
"...Q",
".Q.."]
]
'''

# Conditions cannot place Queen:
# Cannot be on the same row by definition, so no need to check
# On same Column : ColumnForRow[i] == ColumnForRow[j]
# On same Diagonal: (ColumnForRow[i] - ColumnForRow[j]) == (i- j) or (ColumnForRow[j] - ColumnForRow[i]) == (i - j)

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def canPlace(row):
            for r in range(0, row):    # check previous rows
                diff = abs(colForRow[r]-colForRow[row])
                if (diff == 0) or (diff == row-r):
                    return False
            return True


        def placeQueen (row, res, result):
            if row == n:   # convert list of list to list of string
                result.append([''.join(r) for r in res])
                return
            else:
                for col in range(0,n):
                    colForRow[row] = col
                    if canPlace(row):   
                        res[row][col]='Q'
                        placeQueen(row+1,res,result)
                        res[row][col]='.'  
                return


        res = [['.']*n for _ in range (n)]
        colForRow = [None for _ in range(n)]
        result = []
        placeQueen(0,res,result)
        return result
