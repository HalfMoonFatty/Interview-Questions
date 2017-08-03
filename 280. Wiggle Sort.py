'''
Problem:

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

'''


'''
Solution: Linear Scan In Place Sort

Time: O(n). In the worst case we swap at most n/2 times. An example input is [2,1,3,1,4,1].
Space: O(1)

'''


class Solution(object):
    def wiggleSort(self, nums):
        """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            
        for i in range(len(nums)-1):     # Note: index boundary
            if i%2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            if i%2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return
