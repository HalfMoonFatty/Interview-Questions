'''
Problem:

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

'''

'''
Solution:

The difficult part is to remove dupliacte.
'''

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index, nums, res, result):
            if len(res) > 1:
                result.append(res[:])
                    
            visited = set()        
            for i in range(index, len(nums)):
                if nums[i] in visited: continue
                if index == 0 or nums[i] >= res[-1]:
                    visited.add(nums[i])
                    res.append(nums[i])
                    dfs(i+1, nums, res, result)
                    res.pop()
         
          
        result = []
        dfs(0, nums, [], result)
        return result
