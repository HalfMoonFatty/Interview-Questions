'''
Problem:

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''



class Solution(object):
    def majorityElement(self, nums):

        candidate = nums[0]
        count = 0
        for elem in nums:
            if count == 0:
                candidate = elem
                count += 1
            else:
                if candidate == elem:
                    count += 1
                else:
                    count -= 1
        return candidate
