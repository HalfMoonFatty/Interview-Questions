'''
Problem:

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. 

If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21

Example 2:
Input: 21
Output: -1
'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        
        if not nums:
            return None

        j = 0
        # Find the first index(j) break the trend: nums[i-1] >= nums[i] 应该前一个比后一个大
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] < nums[i]:
                j = i-1
                break

        # Find the smallest number which is larger than nums[j], the break point
        if j >= 0:
            for i in range(len(nums)-1, j, -1):
                if nums[i] > nums[j]:    # 找到第一个比 nums[j] 大的 nums[i]
                    nums[j], nums[i] = nums[i], nums[j]    # swap position
                    break
        
        # Reverse the rest
        nums[j+1:] = nums[j+1:][::-1]
        ans = int(''.join(nums))
        return n < ans <= 0x7FFFFFFF and ans or -1
