'''
Problem:
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

For example:
    A = [2,3,1,1,4], return true.
    A = [3,2,1,0,4], return false.
'''

'''
Solution:
注意题目中A[i]表示的是在位置i，“最大”的跳跃距离，而并不是指在位置i只能跳A[i]的距离。
遍历nums数组，update maxCoverage 试图reach 最后一个Index
同时在遍历过程中如果发现一点不能被已有的maxCoverage覆盖，那么说明有“断点”，到不了最后
'''

class Solution(object):
    def canJump(self, nums):
        """
            :type nums: List[int]
            :rtype: bool
            """
        maxCoverage = 0
        for i in range(0, len(nums)):
            if i > maxCoverage:
                break
            maxCoverage = max(maxCoverage, i+nums[i])

        return maxCoverage >= len(nums)-1

