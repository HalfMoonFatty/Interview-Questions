'''
Problem:

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example, Given nums = [0, 1, 3] return 2.

Note: Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''

'''
Solution1: 等差数列前n项和 - 数组之和
'''

class Solution(object):
    def missingNumber(self, nums):
 
        n = len(nums)
        sum1 = (n*(n+1))/2
        sum2 = sum(nums)
        return sum1-sum2
        
        
        
# Solution 2: XOR

class Solution(object):
    def missingNumber(self, nums):

        res = i = 0 
        while i < len(nums):
            res = res ^ i ^ nums[i]
            i += 1       
        return res ^ i
