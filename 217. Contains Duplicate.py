'''
Problem:

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

'''

'''
Solution:

Time: O(N)
Space: O(N)
'''

from sets import Set
class Solution(object):
    def containsDuplicate(self, nums):
        """
            :type nums: List[int]
            :rtype: bool
            """
        set = Set()
        for n in nums:
            if n in set:
                return True
            else:
                set.add(n)
        return False
