'''
Problem:

Numbers keep coming, return the median of numbers at every time a new number added.

Clarification
What's the definition of Median?
- Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

'''
import heapq

class Solution:

    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
            
    def findMedian(self):
        if len(self.small) == len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
            
    def medianII(self, nums):
        res = []
        for n in nums:
            self.addNum(n)
            res.append(self.findMedian())
        return res
