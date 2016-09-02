'''
Problem:

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

Hint: Try to solve it in one dimension first. How can this solution apply to the two dimension case?

'''


class Solution(object):
    def minTotalDistance(self, grid):
        """
            :type grid: List[List[int]]
            :rtype: int
            """
        row = []
        col = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)

        row.sort()
        col.sort()
        rmid = len(row)/2
        cmid = len(col)/2
        ret = 0
        for r in row:
            ret += abs(r-row[rmid])
        for c in col:
            ret += abs(c-col[cmid])
        return ret

'''
Solution: Pythonic way of programming
'''

class Solution(object):
    def minTotalDistance(self, grid):
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        sumr = [i for i in xrange(r) for j in xrange(c) if grid[i][j]]
        sumc = [j for i in xrange(r) for j in xrange(c) if grid[i][j]]
        sumr.sort()
        sumc.sort()
        mid_row = sumr[len(sumr)/2]
        mid_col = sumc[len(sumc)/2]
        return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])
