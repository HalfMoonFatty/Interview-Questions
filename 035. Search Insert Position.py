'''
Problem:

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''



class Solution(object):
    def searchInsert(self, nums, target):

        start, end = 0, len(nums)-1
        
        while start < end:    # note < not <=
            mid = start + (end-start)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
                
        if target <= nums[start]:  # note <=
            return start
        else:
            return start+1
