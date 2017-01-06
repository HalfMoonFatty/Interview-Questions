'''
Problem:

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

    Example 1:
    Given nums = [1, -1, 5, -2, 3], k = 3,
    return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

    Example 2:
    Given nums = [-2, -1, 2, 1], k = 1,
    return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
	Can you do it in O(n) time?
'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
        mp = {}
        sums = 0
        maxLen = 0
        for i in range(len(nums)):
            sums += nums[i]
            if not mp.has_key(sums):
                mp[sums] = i   # mp stores index
                
            if sums == k:
                maxLen = i + 1
            elif mp.has_key(sums - k):
                maxLen = max(maxLen, i-(mp[sums - k]))  # note: NOT i-(mp[sum - k])+1

        return maxLen


