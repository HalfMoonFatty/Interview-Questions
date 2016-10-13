'''
Problem:

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
'''



'''
Solution:

Time: O(mn) time
Space: O(n) space.
'''

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
            :type grid: List[List[str]]
            :rtype: int
            """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0


        rowCache = 0
        colCache = [0]*len(grid[0])
        maxHit = 0

        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == "W":
                    rowCache = 0
                    for k in range(j,n):
                        if grid[i][k] == "W":
                            break
                        if grid[i][k] == "E":
                            rowCache += 1


                if i == 0 or grid[i-1][j] == "W":
                    colCache[j] = 0
                    for k in range(i,m):
                        if grid[k][j] == "W":
                            break
                        if grid[k][j] == "E":
                            colCache[j] += 1


                if grid[i][j] == "0":
                    maxHit = max(maxHit,rowCache+colCache[j])

       return maxHit
