'''
Problem:

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. 
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
'''


class Solution(object):

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
            
        def addNum(n):
            if len(small) > 0 and n <= -small[0]:
                heapq.heappush(small, -n)
                balance[0] += 1
            else:
                heapq.heappush(large, n)
                balance[0] -= 1
            return
        
        
        def removeNum(n):
            if len(small) > 0 and n <= -small[0]:
                balance[0] -= 1
                if n == -small[0]: heapq.heappop(small)
                else: invalidMap[n] += 1
            else:
                balance[0] += 1
                if n == large[0]: heapq.heappop(large)
                else: invalidMap[n] += 1
            return
        
        
        def rebalance():
            # rebalance first!
            if balance[0] < 0: # large has more numbers
                heapq.heappush(small, -heapq.heappop(large))
            elif balance[0] > 0: 
                heapq.heappush(large, -heapq.heappop(small))
            # remove out of date numbers
            while len(small) > 0 and invalidMap[-small[0]] > 0: 
                invalidMap[-small[0]] -= 1
                heapq.heappop(small)
            while len(large) > 0 and invalidMap[large[0]] > 0:
                invalidMap[large[0]] -= 1
                heapq.heappop(large)
            # reset balance to 0
            balance[0] = 0
            return
        
        
        def getMedian():
            return float(large[0]) if k % 2 else (large[0] - small[0])/2.0
        
        
        
        medians = []
        invalidMap = collections.defaultdict(int)
        balance = [0]
        
        # init small and large heap
        small, large = [], []    # small is Max heap; large is Min heap
        for i in range(k):
            heapq.heappush(large, nums[i])
        for _ in range(k/2):
            heapq.heappush(small, -heapq.heappop(large))
        # get first median before sliding the window
        medians.append(getMedian())
        
        for i in range(k,len(nums)):
            addNum(nums[i])
            removeNum(nums[i-k])
            rebalance()
            medians.append(getMedian())    
        return medians
        
