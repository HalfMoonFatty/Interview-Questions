'''
Problem:

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. 
Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.

'''


'''
Solution: 二分查找（Binary Search）

从数组递增有序和O(log n)时间复杂度推断，题目可以采用二分查找求解。

初始令左、右指针lo, hi分别指向0, len(nums) - 1

当lo < hi时执行循环：

令mi = (lo + hi) / 2

若nums[mi] == nums[mi - 1]：数组可以分为[lo, mi - 2], [mi + 1, hi]两部分，目标元素位于长度为奇数的子数组中。

同理，若nums[mi] == nums[mi + 1]：数组可以分为[lo, mi - 1], [mi + 2, hi]两部分，目标元素位于长度为奇数的子数组中。

若nums[mi]与nums[mi - 1], nums[mi + 1]均不相等，则返回nums[mi]

'''

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1    
        while start < end:
            mid = start + (end-start)/2
            
            if nums[mid] == nums[mid-1]:
                if (mid-1)%2: # left part length is odd
                    end = mid-2
                else:
                    start = mid+1
                    
            elif nums[mid] == nums[mid+1]:
                if (mid+1)%2: # right part length is odd
                    start = mid+2
                else:
                    end = mid-1
                    
            else: return nums[mid]
            
        return nums[start]
        
