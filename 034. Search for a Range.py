'''
Problem:

    Given a sorted array of integers, find the starting and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].

For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
'''

'''
Solution:

Time O(logn)
Space O(n)

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        # Search for left bound.
        i, j = 0, len(nums) - 1
        result = [-1, -1]
        while i < j:
            mid = (i + j) / 2  # Biased to left, so j = mid can still advance.
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] != target:
            return [-1, -1]
        result[0] = i
        
        # Search for right bound.
        j = len(nums) - 1
        while i < j:
            mid = (i + j) / 2 + 1  # Bais to right, so i = mid can still advance.
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        result[1] = j
        
        return result

'''
class Solution(object):
    def searchRange(self, nums, target):

        def binSearch(nums, start, end, target):
            if start > end:
                return

            mid = start + (end - start)/2
            if nums[mid] == target:
                if self.rangepair == [-1,-1]:
                    self.rangepair = [mid, mid]
                elif mid < self.rangepair[0]:
                    self.rangepair[0] = mid
                elif mid > self.rangepair[1]:
                    self.rangepair[1] = mid
                # Search left boundary of target
                binSearch(nums, start, mid-1, target)
                # Search right boundary of target
                binSearch(nums, mid+1, end, target)
            elif nums[mid] < target:
                binSearch(nums, mid+1, end, target)
            else:
                binSearch(nums, start, mid-1, target)

        self.rangepair = [-1,-1]
        binSearch(nums, 0, len(nums)-1, target)
        return self.rangepair
'''
