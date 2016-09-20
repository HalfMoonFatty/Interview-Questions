'''
Problem:


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

'''


# Solution 1: Binary Indexed Tree





# Solution 2: Segment Tree

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        h = int(math.ceil(math.log(self.size, 2))) if self.size else 0
        segTreeSize = 2**(h+1) - 1
        self.segTree = [0] * segTreeSize
        if self.size: self.initSegTree(0, self.size-1,0)
        
        
    
    def initSegTree(self, start, end, pos):
        if start == end: 
            self.segTree[pos] = self.nums[start]
        else:
            mid = (start+end)/2
            self.segTree[pos] = self.initSegTree(start, mid, pos*2+1) + self.initSegTree(mid+1, end, pos*2+2)
        return self.segTree[pos]
    
    
    def updateSegTree(self, start, end, index, delta, pos):
        if index < start or index > end: return
    
        self.segTree[pos] += delta
        
        if start != end: 
            mid = (start+end)/2
            self.updateSegTree(start, mid, index, delta, pos*2+1)
            self.updateSegTree(mid+1, end, index, delta, pos*2+2)
        return
    
    
    def sumRangeSegTree(self, start, end, qstart, qend, pos):
        # case 1: total overlap
        if qstart <= start and end <= qend:
            return self.segTree[pos]
        # case 2: no overlap
        if end < qstart or start > qend:
            return 0 
        # case 3: partial overlap
        mid = (start+end)/2
        return self.sumRangeSegTree(start, mid, qstart, qend, pos*2+1) + self.sumRangeSegTree(mid+1, end, qstart, qend, pos*2+2)



    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i < 0 or i >= self.size: return
        delta = val - self.nums[i]
        self.nums[i] = val
        self.updateSegTree(0, self.size-1, i, delta, 0)
        
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or j < 0 or i >= self.size or j >= self.size: return 0
        return self.sumRangeSegTree(0, self.size-1, i, j , 0)
