'''
Problem:

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note: Both the array size and each of the array element will not exceed 100.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

'''

'''
Solution 1: DFS

Time: O(n^2)
Space: O(n)
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canPart(start, nums, sums):
            if sums < 0: return False
            if sums == 0: return True
            for i in range(start,len(nums)):
                if canPart(i+1, nums, sums-nums[i]): 
                    return True
            return False
        
        sums = sum(nums)
        return False if sums%2 else canPart(0, nums, sums/2)
        
 

'''
Solution 2: DP

Time: O(M*N) (N is half of array sum）
Space:O(N)

'''

import sys
class Solution(object):
    def canPartition(self, nums):
        
        sums = sum(nums)
        if sums%2: return False  
        
        sums /= 2
        dp = [-sys.maxint+1] * (sums+1)
        dp[0] = 0
        for n in nums:
            for s in range(sums,n-1,-1):
                dp[s] = max(dp[s-n]+1, dp[s])
        return dp[-1] > 0
        
        
