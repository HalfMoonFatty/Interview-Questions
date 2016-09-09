'''
Problem:

	Given an array of non-negative integers, you are initially positioned at the first index of the array.
	Each element in the array represents your maximum jump length at that position.
	Your goal is to reach the last index in the minimum number of jumps.

	For example: 
	Given array A = [2,3,1,1,4]
	The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

	Note: You can assume that you can always reach the last index.
'''


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curMaxIndex,lastMaxIndex = 0,0
        njumps = 0
        i = 0 
        
        while curMaxIndex < len(nums)-1:
            lastMaxIndex = curMaxIndex
            while i <= lastMaxIndex:    # cannot use for loop
                curMaxIndex = max(curMaxIndex,i+nums[i])
                i += 1
            njumps += 1
            if curMaxIndex == lastMaxIndex:
                return -1
            
        return njumps
            
