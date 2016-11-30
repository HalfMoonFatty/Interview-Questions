'''
Problem:

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
     [
         [2],
        [3,4],
       [6,5,7],
     [4,1,8,3]
     ]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''


'''
Solution: Bottom Up - 越走越窄所以不用担心index out of range. 而且最后只有一个element，不需要重新比较取最小值。

从倒数第二行开始扫描，每一个位置能取得的最小值(total[j])是：
total[j](current value) = triangle[i][j] + min(total[j](orignal value),total[j+1](original value))

Time: O(N) N - number of element in the triangle
Space: O(n)
'''



class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if len(triangle) < 2:
            return triangle[0][0]

        lastrow = triangle[-1][:]

        # from the 2nd last row:
        for i in range(len(triangle)-2, -1, -1):
            currow = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                currow[j] = triangle[i][j] + min(lastrow[j],lastrow[j+1])
            lastrow = currow
        return lastrow[0]

	
	
# can be optimized to not using current row

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if len(triangle) < 2:
            return triangle[0][0]

        lastrow = triangle[-1][:]

        # from the 2nd last row:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                lastrow[j] = triangle[i][j] + min(lastrow[j],lastrow[j+1])
        return lastrow[0]    
