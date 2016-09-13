'''
Problem:

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

'''

# Solution 1: O(n^2)

class Solution(object):
    def lengthOfLIS(self, nums):

        if not nums: return 0
        
        dp = [1] * len(nums)
        maxLen = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(maxLen,dp[i])
        return maxLen
        
        
        
        
# Solution 2: O(n log n)
# seqLengthTail records the last element at different lengths
# seqLengthTail[i] is the last element for a sequence length of i+1

import sys
class Solution(object):
    def lengthOfLIS(self, nums):

        if not nums: return 0
        
        n = len(nums)
        seqLengthTail = [sys.maxint] * (n+1)      # init with maxint length from 1 to n
        maxLen = 1
        
        for i in range(1,n+1):
            ind = bisect.bisect_left(seqLengthTail,nums[i-1])
            seqLengthTail[ind] = nums[i-1]
            maxLen = max(maxLen, ind+1)
            
        return maxLen
                
