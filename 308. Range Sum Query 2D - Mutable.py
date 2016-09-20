'''
Problem:


Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
    Given matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    update(3, 2, 2)
    sumRegion(2, 1, 4, 3) -> 10

Note:
    The matrix is only modifiable by the update function.
    You may assume the number of calls to update and sumRegion function is distributed evenly.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

'''



class NumMatrix(object):
    def __init__(self, matrix):

        if not matrix or len(matrix[0]) == 0 or len(matrix) == 0:
            return

        self.m = len(matrix)
        self.n = len(matrix[0])
        self.tree = [[0 for j in range(self.n+1)] for i in range(self.m+1)]
        self.num = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i,j,matrix[i][j])



    def update(self, row, col, val):
        if self.m == 0 or self.n == 0:
            return
        delta = val - self.num[row][col]
        self.num[row][col] = val
        i = row+1
        while i <= self.m:
            j = col+1
            while j <= self.n:
                self.tree[i][j] += delta
                j += (j & -j)
            i += (i & -i)
        return



    def sumRegion(self, row1, col1, row2, col2):

        def sum(row,col):
            accu = 0
            i = row
            while i > 0:
                j = col
                while j > 0:
                    accu += self.tree[i][j]
                    j -= (j & -j)
                i -= (i & -i)
            return accu


        if self.m == 0 or self.n == 0:
            return 0
        return sum(row2+1, col2+1) - sum(row1, col2+1) - sum(row2+1, col1) + sum(row1, col1)

