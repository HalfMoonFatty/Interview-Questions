'''
Problem:
    Given an unsorted integer array, find the first missing positive integer.

    For example,
    Given [1,2,0] return 3,
    and [3,4,-1,1] return 2.

    Your algorithm should run in O(n) time and uses constant space.

'''


# Time: O(n)
# Space: O(1)
# 尽量使 nums[i] == i+1
# 第一个下标+1与数值不同的数字，即为所求。或者遍历完整个nums 都是从1开始连贯的，那么就是len(nums)+1


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def swap(nums, i, j):
            a = nums[i]
            b = nums[j]
            nums[i] = b
            nums[j] = a
            
            
        n = len(nums)
        if not n: return 1
        
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                swap(nums, i, nums[i]-1)
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
                
        return n+1
