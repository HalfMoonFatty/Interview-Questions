'''
Problem:

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

'''

'''
Solution:

Complexities:
Time: O(n)
Space: O(1)
'''

import sys
class Solution(object):
    def increasingTriplet(self, nums):

        i = j = sys.maxint
        for n in nums:
            if n <= i:         # n is better than the 1st candidate (i), store it
                i = n
            elif n <= j:       # n is better than the current 2nd candidate (j), store it
                j = n
            else:              
                return True    
        return False





