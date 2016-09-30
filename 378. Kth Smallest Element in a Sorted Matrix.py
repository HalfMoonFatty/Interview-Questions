'''
Problem:

    Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
[ 1,  5,  9],
[10, 11, 13],
[12, 13, 15]
],
k = 8,

return 13.

Note:
    You may assume k is always valid, 1 ≤ k ≤ n2.
     
'''



# Solution 1: Heap

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
        minheap = []

        # init the minheap with first element in the first row
        for j in range(len(matrix[0])):
            heapq.heappush(minheap, (matrix[0][j],0,j))

        for n in range(k-1):
            t = heapq.heappop(minheap)
            r,c = t[1],t[2]
            if r == len(matrix)-1: continue  # last row, this col has been finished
            heapq.heappush(minheap, (matrix[r+1][c],r+1,c))

        return heapq.heappop(minheap)[0]

    
    
    
# Solution 2: Binary Search (similar to 287.Find the Duplicate Number)

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
        minVal,maxVal = -sys.maxint-1,sys.maxint
        midVal = 0
        n = len(matrix)

        while minVal < maxVal:
            midVal = minVal + (maxVal-minVal)/2
            count = 0
            for i in range(n):
                pos = bisect.bisect_right(matrix[i], midVal)
                count += pos

            if count < k:
                minVal = midVal+1

            else:
                maxVal = midVal

        return minVal
        
