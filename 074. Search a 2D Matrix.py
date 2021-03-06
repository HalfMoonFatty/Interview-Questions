'''
Problem:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:
[
[1,   3,  5,  7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
Given target = 3, return true.

'''


'''
Solution 1: Don't treat it as a 2D matrix, just treat it as a sorted list

    Use binary search.
    n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
    an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];
'''

class Solution(object):
    def searchMatrix(self, matrix, target):

        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m*n-1
       
        while start <= end:
            mid = (start + end)/2
            if target == matrix[mid/n][mid%n]:
                return True
            elif target > matrix[mid/n][mid%n]:
                start = mid + 1
            else:
                end = mid - 1
       
        return False




# Solution 2 - 1: Iterative Implementation; The tricky part is to start from the left up corner.

class Solution(object):
    
    def searchMatrix(self, matrix, target):

        i = 0
        j = len(matrix[0])-1
       
        while i <= len(matrix)-1 and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False

