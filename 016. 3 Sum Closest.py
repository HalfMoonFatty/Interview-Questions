'''
Problem:

	Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
	Return the sum of the three integers. You may assume that each input would have exactly one solution.

	For example,
    given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

import sys
class Solution(object):
    def threeSumClosest(self, nums, target):

        if len(nums)<3:
            return []

        nums.sort()
        res = 0
        mindiff = sys.maxint

        for i in range(0,len(nums)-2):
            curtar = target - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                diff = curtar - nums[left] - nums[right]
                if abs(diff) < mindiff:
                    mindiff = abs(diff)    # update the mindiff, always >= 0
                    res = nums[i] + nums[left] + nums[right]   

                if nums[left] + nums[right] < curtar:
                    left += 1
                else:
                    right -= 1

        return res
