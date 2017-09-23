'''
Problem:

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

'''


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = [1] * len(nums)
        count = [1] * len(nums)
        res = maxLen = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        count[i] += count[j]
                    elif length[i] < length[j] + 1:
                        length[i] = length[j]+1
                        count[i] = count[j]
                        
                        
            if maxLen == length[i]: 
                res += count[i]
            elif length[i] > maxLen: 
                maxLen = length[i]
                res = count[i]
        return res
                
                
                
