'''
Problem:

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

For example:

add(1)
add(2)
findMedian() -> 1.5

add(3)
findMedian() -> 2

'''

'''
Note:
    small heap is a min heap
    large heap is a max heap
'''

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num)) # note: -num
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0]-self.small[0])/2.0  # note: float
        else:
            return float(self.large[0])
