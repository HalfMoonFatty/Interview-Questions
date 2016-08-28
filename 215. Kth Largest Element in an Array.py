'''
Problem:

	Find the kth largest element in an unsorted array. 
	Note that it is the kth largest element in the sorted order, not the kth distinct element.
	For example,Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1,nums2 = [],[]
        for n in nums:
            if n > pivot:
                nums1.append(n)
            elif n < pivot:
                nums2.append(n)
            # else: pivot found
            # do nothing
        if k <= len(nums1):    
            return self.findKthLargest(nums1, k)
        elif k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot
