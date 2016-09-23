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

        def countNQueens(row):
            if row == n:
                return 1        # finished one entire game, return 1
            count = 0
            for col in range(0,n):
                colForRow[row] = col
                if isValid(row):
                    count += countNQueens(row+1)  # add up all possbile solutions in the subtree
            return count

        colForRow = [None for i in range(0,n)]
        return countNQueens(0)
