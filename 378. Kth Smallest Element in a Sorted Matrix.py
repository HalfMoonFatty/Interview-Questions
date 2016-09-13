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
