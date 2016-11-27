'''
Problem:

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example, Given the following matrix:
[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

'''
Solution:

Time: O(n^2)
Space: O(n^2)

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
        res = []
        if len(matrix) == 0:
            return res

        rowBegin, rowEnd = 0, len(matrix)-1
        colBegin, colEnd = 0, len(matrix[0])-1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Scan the top row:
            for j in range(colBegin, colEnd+1):
                res.append(matrix[rowBegin][j])
            rowBegin += 1

            # Scan the right col:
            for i in range(rowBegin, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            # Scan the bottom row:
            if rowBegin <= rowEnd:    # check !!!
                for j in range(colEnd, colBegin-1, -1):
                    res.append(matrix[rowEnd][j])
            rowEnd -= 1

            # Scan the left col:
            if colBegin <= colEnd:    # check !!!
                for i in range(rowEnd, rowBegin-1, -1):
                    res.append(matrix[i][colBegin])
            colBegin += 1

        return res
