class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        h = int(math.ceil(math.log(self.size, 2))) if self.size else 0
        STsize = 2**(h+1) - 1
        self.segTree = [0] * STsize
        if self.size: self.initSegTree(0, self.size-1,0)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i < 0 or i >= self.size: return
        self.nums[i] = val
        delta = val - self.nums[i]
        self.updateSegTree(0, self.size-1, i, delta, 0)
        
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or j < 0 or j > len(self.nums)-1 or j > len(self.nums)-1: return 0
        return self.sumRangeSegTree(0, self.size-1, i, j , 0)
        
    
    
    def initSegTree(self, ststart, stend, pos):
        if ststart == stend: 
            self.segTree[pos] = self.nums[ststart]
        else:
            mid = (ststart+stend)/2
            self.segTree[pos] = self.initSegTree(ststart, mid, pos*2 + 1) + self.initSegTree(mid+1, stend, pos*2 + 2)
        return self.segTree[pos]
    
    
    def updateSegTree(self, ststart, stend, index, delta, pos):
        if index < ststart or index > stend: return
        if ststart == stend: 
            self.segTree[pos] += delta
        else:
            mid = (ststart+stend)/2
            self.updateSegTree(ststart, mid, index, delta, pos)
            self.updateSegTree(mid+1, stend, index, delta, pos)
        return
    
    
    def sumRangeSegTree(self, ststart, stend, qstart, qend, pos):
        # case 1: total overlap
        if ststart <= qstart and stend >= qend:
            return self.segTree[pos]
        # case 2: no overlap
        if stend < qstart or sstart > qend:
            return 0 
        # case 3: partial overlap
        mid = (ststart+stend)/2
        return self.sumRangeSegTree(ststart, mid, qstart, qend, pos*2+1) + self.sumRangeSegTree(mid+1, stend, qstart, qend, pos*2+2)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
