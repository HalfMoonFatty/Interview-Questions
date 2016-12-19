'''
Problem 1:

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example, Given heights = [2,1,5,6,2,3], return 10.
'''

import sys
class Solution(object):
    def largestRectangleArea(self, heights):
        
        if not heights: return 0

        maxArea = 0
        index = []         
        heights.append(0)   # Note: sentinel node

        for i in range(len(heights)):
            while len(index)>0 and heights[index[-1]] >= heights[i]:   # Note: >=
                h = heights[index.pop()]
                if len(index) > 0: startInd = index[-1]
                else: startInd = -1
                maxArea = max(maxArea,h*(i-startInd-1))

            index.append(i)

        return maxArea
     


'''
Problem 2:
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
'''

class Solution(object):
    def maximalRectangle(self, matrix):

        if not matrix: return 0
        m,n = len(matrix),len(matrix[0])

        height = [0]*(n+1)     # height[n+1] is sentinel node
        maxArea = 0

        for i in range(m):    # i iterate through number of rows
            index = []
            for j in range(n+1):  # Note n+1 as j iterate through height
                if j < n:
                    if matrix[i][j] == '1': height[j] += 1
                    else: height[j] = 0  # reset height back to 0

                # calculate maxArea
                while len(index)>0 and height[index[-1]] >= height[j]:
                    h = height[index.pop()]    
                    if len(index) > 0: startInd = index[-1] 
                    else: startInd = -1
                    maxArea = max(maxArea,h*(j-startInd-1))
                    
                index.append(j)
                
        return maxArea
