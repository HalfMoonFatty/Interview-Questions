'''
Problem:
   
    Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
   
Example:
    (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
    (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
   
Note:
    You may assume all input has valid answer.
   
Follow Up:
    Can you do it in O(n) time and/or in-place with O(1) extra space?

'''

'''
Solution (Linear Solution in place):
   
    Find the median – O(n) time
    Partition the array into 3 parts by smaller than, equal to or larger than the median O(n) time
    One-pass three-way partition to rearrange all elements in place
   
    (1) Elements that are larger than the median: we can put them in the first few odd slots;
    (2) Elements that are smaller than the median: we can put them in the last few even slots;
    (3) Elements that equal the median: we can put them in the remaining slots.
   
   
    Re-map the indices into its "destined indices", odd indices first and even indices follow.
   
    Example:
    Original Indices:      0  1  2  3  4  5  6  7  8  9 10 11
    Mapped Indices:        1  3  5  7  9 11  0  2  4  6  8 10
    
    Reversed mapping:
    Mapped Indices:        0  1  2  3  4  5  6  7  8  9 10 11
    Original Indices:      6  0  7  1  8  2  9  3 10  4 11  5   (wiggled)
  
  
    def map_index(i):
        return (i*2+1)%(len(nums)|1)
    where (n | 1) calculates the nearest odd that is not less than n.
    i.e. 把偶数变成比他大一个的奇数
    n = 12, n|1 = 13
    n = 11, n|1 = 11
   
   
Complexities: (On the condition that finding median is O(n)-time and O(1)-space)
    Time: O(n)
    Space: O(1)
   
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def findKthLargest(nums, k):
            if not nums: return
            pivot = random.choice(nums)
            nums1,nums2 = [],[]
            for n in nums:
                if n > pivot:
                    nums1.append(n)
                elif n < pivot:
                    nums2.append(n)

            if k <= len(nums1):                # check if nums1 covers Kth element
                return findKthLargest(nums1, k)
            elif k > len(nums) - len(nums2):   # Cannot use len(nums) - len(nums) 
                return findKthLargest(nums2, k - (len(nums) - len(nums2)))
            return pivot

            
        def map_index(i):
            return (i*2+1)%(len(nums)|1)
       
       
        # 3 way partition
        median = findKthLargest(nums, len(nums)/2)
       
        itr = 0
        Left,Right = 0,len(nums) - 1
        while itr <= Right:
            if nums[map_index(itr)] > median:
                nums[map_index(Left)], nums[map_index(itr)] = nums[map_index(itr)], nums[map_index(Left)]
                Left += 1
                itr += 1
            elif nums[map_index(itr)] < median:
                nums[map_index(Right)], nums[map_index(itr)] = nums[map_index(itr)], nums[map_index(Right)]
                Right -= 1
            else:
                itr += 1
       
        return        
