Problem:

	Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

	All elements < k are moved to the left
	All elements >= k are moved to the right
	Return the partitioning index, i.e the first index i nums[i] >= k.

Note:

	- You should do really partition in array nums instead of just counting the numbers of integers smaller than k.
	- If all elements in nums are smaller than k, then return nums.length

'''

class Solution:

    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
