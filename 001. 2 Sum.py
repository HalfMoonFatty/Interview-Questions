'''
Problem:

	Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution.

	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
	
	The return format had been changed to zero-based indices. Please read the above updated description carefully.

'''
class Solution(object):
    def twoSum(self, nums, target):

        mp = {}

        for i in range(len(nums)):
            if mp.has_key(target-nums[i]):
                return [mp[target-nums[i]], i]
            else:
                mp[nums[i]] = i
