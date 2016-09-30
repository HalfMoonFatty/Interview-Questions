'''
Problem:

    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?
    Would this affect the run-time complexity? How and why?

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    The array may contain duplicates.

'''

'''
Solution: 

For case where AL == AM == AR, the minimum could be on AM’s left or right side (eg, [1, 1, 1, 0, 1] or [1, 0, 1, 1, 1]). 
In this case, we could not discard either subarrays and therefore such worst case degenerates to the order of O(n).

'''

class Solution(object):
    def findMin(self, nums):

        L, R = 0, len(nums)-1
        
        while L < R and nums[L] >= nums[R]:
            M = L+(R-L)/2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[L]:
                R = M
            else:   # nums[L] == nums[M] == nums[R]
                L = L + 1
                
        return nums[L]




# Direct Linear Scan may not be as efficient as the above solution

class Solution:

    def findMin(self, num):
        localMin = num[0]
        for i in num:
            if i < localMin:
                localMin = i
        return localMin
