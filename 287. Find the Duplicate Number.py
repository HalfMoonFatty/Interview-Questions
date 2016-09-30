'''
Problem:

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''



# Time: O nlog(n)

class Solution(object):

    def findDuplicate(self, nums):

        start, end = 1, len(nums)   # [start,end)

        while start <= end:
            count = 0
            mid = start + (end-start)/2   # mid is a number not index
            for n in nums:
                if n <= mid:    # note it is " <= "
                    count += 1
            if count > mid:
                end = mid - 1
            else:
                start = mid + 1
        return start
        
