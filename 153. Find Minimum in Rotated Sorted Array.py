'''
Problem:

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    You may assume no duplicate exists in the array.

'''

# Time complexity is O(log n).


class Solution(object):
    
    def findMin(self, nums):

        L,R = 0,len(nums)-1
        
        while L < R and nums[L] >= nums[R]:   # note >=
            M = L+(R-L)/2
            if nums[M] > nums[R]:
                L = M + 1    # M+1
            else: 
                R = M        # M
                
        return nums[L]    # when L == R, we have found the minimum element
                  
