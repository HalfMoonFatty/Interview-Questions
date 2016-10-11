'''
Problem:

    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
    Did you use extra space?
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

'''




'''
Solution 1:

Time: O(n^2)
Space: O(m + n)

'''


class Solution(object):
    def setZeroes(self, matrix):

        if matrix == None:
            return

        row_bitMap = [0]*len(matrix)
        col_bitMap = [0]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_bitMap[i] = 1
                    col_bitMap[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row_bitMap[i] == 1 or col_bitMap[j] == 1:
                    matrix[i][j] = 0

        return

    
    
    
'''
Solution 2: Optimization

Time: O(n^2)
Space: O(1)
'''
    
    
class Solution(object):
    def setZeroes(self, matrix):

        m,n = len(matrix), len(matrix[0])
        col0 = 1
        
        # top-down
        for i in range(m):
            if matrix[i][0] == 0: col0 = 0   
            for j in range(1,n):        # j count up from 1
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # bottom-up
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):   # j count down to 1
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0: matrix[i][0] = 0  
        return        
    
