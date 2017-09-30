'''
Problem:

Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.

     Example:

A = [
     [ 1, 0, 0],
     [-1, 0, 3]
     ]

B = [
     [ 7, 0, 0 ],
     [ 0, 0, 0 ],
     [ 0, 0, 1 ]
     ]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

'''



# Solution 1: direct calculation

class Solution(object):
    def multiply(self, A, B):

        # result is len(A) * len(B[0])
        res = [[0 for j in range(len(B[0]))] for i in range(len(A))]

        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    # check every elements(column) in B[k] row:
                    for j in range(len(B[0])):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k]*B[k][j]

        return res




# Optimization: Preload Hash Table of Matrix A and B

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n = len(A), len(A[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        l = len(B[0])
        
        cache_A = collections.defaultdict(collections.defaultdict)
        cache_B = collections.defaultdict(collections.defaultdict)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    cache_A[i][j] = A[i][j]
                    
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]:
                    cache_B[i][j] = B[i][j]
                    
        C = [[0 for j in range(l)] for i in range(m)]
        for i in cache_A:
            for k in cache_A[i]:
                if k in cache_B: 
                    for j in cache_B[k]:
                         C[i][j] += cache_A[i][k] * cache_B[k][j]
        return C




# Solution 2: Preload Hash Table of Matrix A

class Solution(object):
    def multiply(self, A, B):
        """
            :type A: List[List[int]]
            :type B: List[List[int]]
            :rtype: List[List[int]]
            """
        # result is len(A) * len(B[0])
        res = [[0 for j in range(len(B[0]))] for i in range(len(A))]

        # pre-load dictA - a hashtable:
        # key is A's column number (B's row number);
        # value is linked list of tuples (colID,non-zero value)
        rowCacheA = collections.defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    rowCacheA[i].append((j,A[i][j]))


        for i in range(len(A)):
            rowA = rowCacheA[i]
            for k in range(len(rowA)):
                colA = rowA[k][0]
                valA = rowA[k][1]
                for j in range(len(B[0])):
                    # colA is rowID of matrix B,
                    if B[colA][j] != 0:
                        res[i][j] += valA * B[colA][j]

        return res
