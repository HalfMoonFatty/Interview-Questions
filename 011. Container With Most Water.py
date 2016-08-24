'''
Problem:

	Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
	n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
	Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note:
    You may not slant the container.
'''

class Solution:

    def maxArea(self, heights):

        maxWater = 0
        i, j = 0, len(heights)-1

        while i < j:
            if heights[i] < heights[j]:
                water = heights[i]*(j-i)
                i += 1
            else:
                water = heights[j]*(j-i)
                j -= 1

            maxWater = max(maxWater,water)

        return maxWater
