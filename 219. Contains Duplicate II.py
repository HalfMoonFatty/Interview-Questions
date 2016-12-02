'''
Problem:

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array, 
such that nums[i] = nums[j] and the difference between i and j is at most k.

'''

'''
Solution 1: 

Time Complexity O(n^2)
Space Complexity O(1)
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        k = min(len(nums),k)    # note
        for i in range(len(nums)-k+1):
            j = i+1
            while j<=i+k and j < len(nums):    # note
                if nums[j] == nums[i]:
                    return True
                j += 1
        return False
        

        

'''
Solution 2: 

Time Complexity O(n)
Space Complexity O(n)
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = dict()
        for i in range(len(nums)):
            index = numDict.get(nums[i])
            if index >= 0 and i - index <= k:
                return True
            else:
                numDict[nums[i]] = i
        return False
        
