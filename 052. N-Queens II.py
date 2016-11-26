'''
Problem: Follow up for N-Queens problem.

    Now, instead outputting board configurations, return the total number of distinct solutions.

'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isValid(row):
            for r in range(0, row):
                diff = abs(colForRow[r]-colForRow[row])
                if (diff == 0) or (diff == row-r):
                    return False
            return True


        def countNQueens(row,count):
            if row == n:
                count[0] += 1
                return        
            for col in range(0,n):
                colForRow[row] = col
                if isValid(row):
                    countNQueens(row+1, count)  
            return 


        colForRow = [None for i in range(0,n)]
        count = [0]
        countNQueens(0,count)
        return count[0]
