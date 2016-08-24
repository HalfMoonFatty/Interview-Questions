'''
Problem:

Given two array of integers(the first array is array A, the second array is array B), 
now we are going to find a element in array A which is A[i], and another element in array B which is B[j], 
so that the difference between A[i] and B[j] (|A[i] - B[j]|) is as small as possible, return their smallest difference.

'''

'''
Solution 1: 2 pointers

O(nlogn) + O(mlogm) + O(n)
'''
import sys

class Solution:

    def smallestDifference(self, A, B):

        A.sort()
        B.sort()
        ans = sys.maxint
        
        j = 0
        for i in range(len(A)):
            while j + 1 < len(B):
                if B[j+1] > A[i]:
                    break
                j += 1
                
            if j < len(B):
                ans = min(ans,abs(B[j]-A[i]))
            if j+1 < len(B):
                ans = min(ans,abs(B[j+1]-A[i]))
                
        return ans
        
'''
Solution 2: Binary Search

O(nlogn) + O(mlogm) + O(nlongm)
'''

import sys,bisect

class Solution:

    def smallestDifference(self, A, B):

        A.sort()
        B.sort()
        ans = sys.maxint

        for i in range(len(A)):
            j = bisect.bisect_left(B,A[i],0,len(B))
            ans = min(ans, abs(B[j-1]-A[i]))
            if j < len(B):
                ans = min(ans, abs(B[j]-A[i]))
        return ans
            
