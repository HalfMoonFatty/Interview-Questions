'''
Problem:

'''

'''
Solution:

let p be the unique problem index for which A[p]>A[p+1]. If this is not unique or doesn't exist, the answer is False or True respectively. 

We analyze the following cases:

If p = 0, then we could make the array good by setting A[p] = A[p+1].
If p = len(A) - 2, then we could make the array good by setting A[p+1] = A[p].
Otherwise, A[p-1], A[p], A[p+1], A[p+2] all exist, and:
    We could change A[p] to be between A[p-1] and A[p+1] if possible, or;
    We could change A[p+1] to be between A[p] and A[p+2] if possible.

Time Complexity: Let N be the length of the given array. We loop through the array once, so our time complexity is O(N).
Space Complexity: We only use p and i, and the answer itself as the additional space. The additional space complexity is O(1).
'''

class Solution(object):
    def checkPossibility(self, A):
        p = None
        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])
