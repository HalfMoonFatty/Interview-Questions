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

        n, m = len(matrix), len(matrix[0])
        start = 0
        end = m*n-1
       
        while start <= end:
            mid = (start + end)/2
            if target == matrix[mid/m][mid%m]:
                return True
            elif target > matrix[mid/m][mid%m]:
                start = mid + 1
            else:
                end = mid - 1
       
        return False



'''
Solution 2 - 1: Iterative Implementation 
    Same as Search a 2D matrix II; The tricky part is to start from the left up corner.
    - if the target is == matrix[i][j]: return "True" directly;
    - elif target > matrix[i][j]: we need larger values, so seach the next row: i += 1
    - else (target < matrix[i][j]): we need smaller values, so search the smaller column: j -= 1
    row range [0,len(matrix)-1]
    column range [len(matrix[0])-1, 0]
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
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




'''
Solution 2 - 2: Recursive Implementation
   
    Don't know why cannot pass Leetcode oj large test cases with Runtime error.
    Could becasue of python maximum recusion stack depth.
'''
   

 class Solution(object):
    def searchMatrix(self, matrix, target):
        """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
       
        def helper(matrix,r,c,target):
            if r < 0 or c < 0 or r > len(matrix)-1 or c > len(matrix[0])-1:
                return False
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                return helper(matrix,r+1,c,target)
            else:
                return helper(matrix,r,c-1,target)
   
        r = 0
        c = len(matrix[0])-1
        return helper(matrix,r,c,target)
