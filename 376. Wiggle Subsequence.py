'''
Problem:

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:
     Can you do it in O(n) time?

'''



'''
Solution 1: Normal DP

Time complexity : O(n^2) Loop inside a loop.
Space complexity : O(n). Two arrays of the same length are used for dp.

'''
class Solution(object):
    def wiggleMaxLength(self, nums):

        if not nums: return 0
        if len(nums) < 2: return 1
       
        up = [1] * len(nums)
        down = [1] * len(nums)
       
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i],down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i],up[j]+1)
       
        return max(up[-1],down[-1])




'''
Solution 2: Linear DP

Time complexity : O(n). Only one pass over the array length.
Space complexity : O(n). Two arrays of the same length are used for dp.

'''
class Solution(object):
    def wiggleMaxLength(self, nums):

        if not nums: return 0
        if len(nums) < 2: return 1
       
        up = [1] * len(nums)
        down = [1] * len(nums)
       
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1]+1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
       
        return max(up[-1],down[-1])



'''
Solution 3: Same as Solution 2 with Space optimized DP

Time complexity : O(n). Only one pass over the array length.
Space complexity : O(1). Constant space is used.

'''
class Solution(object):
    def wiggleMaxLength(self, nums):

        if not nums: return 0
        if len(nums) < 2: return 1
       
        up = 1
        down = 1
       
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up = max(up,down+1)
            elif nums[i] < nums[i-1]:
                down = max(down,up+1)
       
        return max(up,down)


