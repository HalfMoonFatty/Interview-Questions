'''
Problem:

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
# Min Heap
# Note: 求 max 用 Min heap 每次淘汰最小的

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):

        count = collections.Counter(nums)
        
        heap = []
        result = []
        
        for key in count.keys():
            if len(heap) < k:
                heapq.heappush(heap,(count[key],key))
            else:
                if count[key] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(count[key],key))
                    
                
        while len(heap)>0:
            result.append(heapq.heappop(heap)[1])
        return result[::-1]

        


# Max Heap
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter()
        for n in nums:
            count[n] -= 1
        
        heap = []
        result = []
        
        for key in count.keys():
            heapq.heappush(heap,(count[key],key))
            if len(heap) > len(count)-k:
                result.append(heapq.heappop(heap)[1])
                
        return result
