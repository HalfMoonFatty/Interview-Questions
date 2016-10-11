'''
Problem:

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example, Given n = 3, You should return the following matrix:
[
[ 1, 2, 3 ],
[ 8, 9, 4 ],
[ 7, 6, 5 ]
]

'''

'''
Solution:

Time: O(n^2)
Space: O(n^2)

'''

class Solution(object):
    def generateMatrix(self, n):
        """
            :type n: int
            :rtype: List[List[int]]
            """

        matrix = [[0 for i in range(n)] for j in range(n)]
        rowBegin,rowEnd  = 0, n-1
        colBegin,colEnd  = 0, n-1
        
        count = 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            # scan the top row
            for j in range(colBegin, colEnd+1):
                matrix[rowBegin][j] = count
                count += 1
            rowBegin += 1

            # scan the right col:
            for i in range(rowBegin, rowEnd+1):
                matrix[i][colEnd] = count
                count += 1
            colEnd -= 1

            # scan the bottom row:
            for j in range(colEnd, colBegin-1, -1):
                matrix[rowEnd][j] = count
                count += 1
            rowEnd -= 1

            # scan the left col:
            for i in range(rowEnd, rowBegin-1, -1):
                matrix[i][colBegin] = count
                count += 1
            colBegin += 1

        return matrix
