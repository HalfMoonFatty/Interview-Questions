'''
Problem:

    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?
    Would this affect the run-time complexity? How and why?
    Write a function to determine if a given target is in the array.

'''


# Solution: If duplicates are allowed, the only way to search is linear scan, so run-time is O(n)

 class Solution(object):
   
    def search(self, nums, target):
       
        for elem in nums:
            if elem == target:
                return True
        return False
