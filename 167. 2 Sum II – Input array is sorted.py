'''
Problem:

	Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

	The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
	Please note that your returned answers (both index1 and index2) are not zero-based.

	You may assume that each input would have exactly one solution.

	Input: numbers={2, 7, 11, 15}, target=9
	Output: index1=1, index2=2

'''
'''
Solution 1: Two pointers 

O(n) runtime, O(1) space

'''

class Solution(object):
    def twoSum(self, nums, target):

        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

        return None
        

'''
Solution 2: Binary search

O(n log n) runtime, O(1) space 

'''

class Solution(object):
    def twoSum(self, nums, target):

        def bsearch(nums, tar, start):
            end = len(nums) - 1
            while start <= end:
                mid = (start + end)/2
                if tar == nums[mid]:
                    return mid
                elif tar > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        for i in range(0, len(nums)) :
            j = bsearch(nums, target - nums[i], i + 1)
            if j != -1:
                return [i+1, j+1]

    return None
