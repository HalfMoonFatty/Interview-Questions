'''
Problem:

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
     Given heights = [2,1,5,6,2,3], return 10.
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
     

