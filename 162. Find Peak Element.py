'''
Problem:

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
     Your solution should be in logarithmic complexity.

'''

'''
Solution: Binary Search

If num[i-1] < num[i] > num[i+1], then num[i] is peak
If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
If num[i-1] > num[i] < num[i+1], then both sides have peak (n is num.length)

Time: O(logN)
'''

class Solution(object):

    def findPeakElement(self, nums):
        
        def isPeak(ind):
            return 0 < ind < len(nums)-1 and nums[ind-1] < nums[ind] and nums[ind] > nums[ind+1]


        nums = [-sys.maxint-1] + nums + [-sys.maxint-1]   # senitel nodes, index need -1
        
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start)/2
            if isPeak(mid): 
                return mid-1    # index-1
            elif nums[mid] > nums[mid+1]:
                end = mid-1
            else:
                start = mid+1
        return




# Solution 2: More consice code

class Solution(object):
    def findPeakElement(self, nums):

        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end - start)/2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid+1
        
        return start
