'''
Problem:

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

'''
Solution: 线性遍历+计数器

统计恰好相隔1个'0'的两个连续1子数组的最大长度之和
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == sum(nums): return sum(nums)
        
        maxLen = len1 = len2 = 0
        for n in nums:
            if n == 1:
                len2 += 1
            else:
                len1, len2 = len2, 0
                
            maxLen = max(maxLen, len1 + len2 + 1)
        return maxLen
