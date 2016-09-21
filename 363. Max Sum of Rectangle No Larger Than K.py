'''
Problem:


Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
[1,  0, 1],
[0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

'''

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """

        if not matrix: return 0

        res = -sys.maxint-1
        for left in range(0,len(matrix[0])):
            tmp = [0] * len(matrix)
            for right in range(left, len(matrix[0])):

                # accumulate current column to tmp
                for i in range(len(matrix)):
                    tmp[i] += matrix[i][right]

                # find the max subarray no more than K
                accuSet = [0]
                curSum,curMax = 0, -sys.maxint -1
                for v in tmp:
                    curSum += v
                    ind = bisect.bisect_left(accuSet,curSum-k)
                    if ind < len(accuSet):
                        curMax = max(curMax,curSum-accuSet[ind])
                    # early return
                    #if curMax == k: return k
                    bisect.insort(accuSet,curSum)

                res = max(res, curMax)

        return res

