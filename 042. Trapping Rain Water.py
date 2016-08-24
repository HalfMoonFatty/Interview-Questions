'''
Problem:

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

'''
Solution 1: 2 pointers

Time: O(n)
Space: O(1)

'''

class Solution(object):
    def trap(self, height):

        if not height or len(height) == 1: return 0

        left,right = 0, len(height)-1
        leftHeight, rightHeight = height[0], height[-1]
        water = 0

        while left < right:
            if leftHeight < rightHeight:
                left += 1
                if leftHeight > height[left]:
                    water += leftHeight - height[left]
                else:
                    leftHeight = height[left]
            else:
                right -= 1
                if rightHeight > height[right]:
                    water += rightHeight - height[right]
                else:
                    rightHeight = height[right]
        return water
