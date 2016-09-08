'''
Problem:

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


Example:
    Given matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12

Note:
    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

Company:
    Google
'''

'''
Solution: 

	DP[i][j] is the sum of nums in area matrix[0][0] to matrix[i][j]
    DP size is (m+1)*(n+1)
    dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + matrix[r-1][c-1]

    Be careful with the index:
    - rowMax, rowMin, colMax and colMin are all refer to the original matrix not the DP matrix
    - dp index is +1 than the original matrix.
'''

class NumMatrix(object):
    def __init__(self, matrix):

        if not matrix or len(matrix[0]) == 0 or len(matrix) == 0:
            return

        self.dp = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for r in range(1, len(matrix)+1):
            for c in range(1, len(matrix[0])+1):
                self.dp[r][c] = self.dp[r-1][c] + self.dp[r][c-1] - self.dp[r-1][c-1] + matrix[r-1][c-1]



    def sumRegion(self, row1, col1, row2, col2):

        rowMin = min(row1,row2)
        rowMax = max(row1,row2)

        colMin = min(col1,col2)
        colMax = max(col1,col2)

        # Be careful with the index. rowMax, rowMin, colMax and colMin are all refer to the original matrix not the DP matrix
        # dp index is +1 than the original matrix. Only max need +1
        return self.dp[rowMax+1][colMax+1] - self.dp[rowMin][colMax+1] - self.dp[rowMax+1][colMin] + self.dp[rowMin][colMin]
