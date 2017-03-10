'''
Problem:

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:
Input: [1,3,2,3,1]
Output: 2

Example2:
Input: [2,4,3,5,1]
Output: 3

Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
'''


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = [n * 2 for n in nums]
        index = {v:i+1 for i, v in enumerate(sorted(set(nums + nums2)))}
        bitree = BIT(len(index))
        count = 0

        for n in nums2[::-1]:
            count += bitree.sum(index[n / 2] - 1)
            bitree.add(index[n], 1)
        return count



class BIT(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)
        
            
    def add(self, index, val):
        while index <= self.n:
            self.sums[index] += val
            index += index & -index
        
        
    def sum(self, index):
        ret = 0
        while index > 0:
            ret += self.sums[index]
            index -= index & -index
            
        return ret
        
