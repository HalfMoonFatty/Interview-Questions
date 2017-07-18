'''
Problem:


You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
'''

'''
Solution: min heap

思路类似于Merge k Sorted Lists

将 (nums[i][0], i, index)依次加入minheap. i 为 list index, index 为 element index in the list

变量max记录当前队列中出现过的最大值

循环直到 minheap 的size < len(nums)

  弹出 minheap 的最小元素 n, i, index = heapq.heappop(heap)，
  
  更新 minVal = n
  
  更新 gap, start, end
  
  将 [nums[i][index+1], i, index+1] 加回 minheap, 更新maxVal

'''



import heapq
import sys

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        maxVal = minVal = 0
        for i in range(len(nums)):
            heapq.heappush(heap,[nums[i][0], i, 0])
            maxVal = max(maxVal, nums[i][0])
        
        start = end = -1
        gap = sys.maxint
        while len(heap) == len(nums):
            n, i, index = heapq.heappop(heap)
            minVal = n
            if maxVal - minVal < gap:
                gap = maxVal - minVal
                start, end = minVal, maxVal

            if index+1 < len(nums[i]):
                heapq.heappush(heap,[nums[i][index+1], i, index+1])
                maxVal = max(maxVal, nums[i][index+1])

                
        return [start, end]
