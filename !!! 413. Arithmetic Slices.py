'''
Problem:

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:
A = [1, 2, 3, 4]
return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
'''


'''
Solution:

For example, if A is [1,2,3,4], then A should be [1,1,1]. 
So for adjusted A, 2 or more continuous same values indicates there is an arithmetic slice in original A. 

If there is N continuous same values in adjusted A, there should be an arithmetic slice with length of N + 1.
Arithmetic slice with length N -> 1 + 2 + 3 + .....+ (N - 2) = (1 + N - 2) * (N - 2) / 2 = (N - 1) * (N - 2) / 2 arithmetic slice(s)
So, when length N + 1 -> (N - 1) * N / 2

https://discuss.leetcode.com/topic/62162/3ms-question-maker-solution-in-cpp-o-n-time-and-in-space

Time: O(N)
Space: O(1) in place
'''
  
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        
        for i in range(len(A)-1):
            A[i] = A[i + 1] - A[i]
        
        result = 0
        length = 1
        for i in range(1,len(A)-1):
            if A[i] != A[i - 1]:
                result += length * (length - 1) / 2
                length = 1
            else:
                length += 1
        
        result += length * (length - 1) / 2
        return result
