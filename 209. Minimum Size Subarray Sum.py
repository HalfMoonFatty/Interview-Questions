'''
Problem:

    Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. 
    If there isn't one, return 0 instead.

    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.

Follow up:

    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

'''
Solution 1:
'''
class Solution:

    def minimumSize(self, nums, s):
        if not nums: return -1

        minSize = sys.maxint  # just initialize to len(nums) + 1 is enough
        sum = 0
        i = j = 0
        while j < len(nums):
            sum += nums[j]
            if sum >= s: # found a valid one, update the minSize
                while i <= j: # try to shrink the current minSize
                    if sum -nums[i]< s:
                        break
                    sum -= nums[i]
                    i += 1  # while we can maintain sum >= s, continue shrink size
                minSize = min(minSize, j-i+1)    # update minSize
            j += 1

        return minSize if minSize <= len(nums) else -1
        
        
        
'''
Solution 2:
'''
class Solution:

    def minimumSize(self, nums, s):

        i, j = 0, 0
        sum = 0
        minLen = len(nums)+1

        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                minLen = min(minLen,j-i) # not j-i+1
            sum -= nums[i]

        return minLen if minLen <= len(nums) else -1
