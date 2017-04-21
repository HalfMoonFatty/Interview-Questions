'''
Problem:

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. 
The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. 
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
Input: 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]

Output: 2

Note:
The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. 
Total number of bricks of the wall won't exceed 20,000.
'''

'''
Solution:

按行累加砖块的长度，统计每块砖的右边界，对边界出现的次数进行计数。

墙壁的的行数 - 出现次数最多的边界个数即为答案。

注意判断每行都只有一块砖的情况。
'''

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = collections.Counter()
        for bricks in wall:
            length = 0
            for b in bricks:
                if length: edges[length] += 1
                length += b
        return len(wall) - max(edges.values() or [0])
