'''
Problem:

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

    Example: Given nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
'''

# Solution:
# sums[0] = 0
# sums[i+1] = sums[i] + nums[i]

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = len(nums)
        self.sums = [0] * (size + 1) # sums[0] = 0
        for x in range(size):
            self.sums[x + 1] += self.sums[x] + nums[x]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        """
        return self.sums[j + 1] - self.sums[i]
