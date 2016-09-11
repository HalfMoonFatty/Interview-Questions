'''
Problem:
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

    For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
    the contiguous subarray [4,−1,2,1] has the largest sum = 6.

'''

'''
Solution 1: 
	Reset sum to 0 when sum < 0
	Time: O(n)
	Space: O(1)
'''
class Solution(object):
    def maxSubArray(self, nums):
    
        maxsum = 0
        sum = 0
    
        for i in range(len(nums)):
            sum += nums[i]
            maxsum = max(maxsum,sum)
            if sum < 0:
                sum = 0    # Reset sum
        return maxsum
        
        

'''
NOTE: 
If the array is all negative numbers, what is the correct behavior? Consider this simple array {-3, -10, -5}. 
You could make a good argument that the maximum sum is either: 
(A) -3 (if you assume the subsequence can’t be empty) 
(B) 0 (the subsequence has length 0) or 
(C) MINIMUM_INT (essentially the error case). 
We went with option B (max sum = 0), but there’s no “correct” answer. This is a great thing to discuss with your interviewer to show how careful you are.
'''

class Solution:

    def continuousSubarraySum(self, A):

        maxSum, curSum = -sys.maxint-1, 0
        start = 0
        ret = [0,0]
        for i in range(len(A)):
            if curSum >= 0:
                curSum += A[i]
            else:
                curSum = A[i]
                start = i
                
            # both cases can update maxSum, allneg case
            if curSum > maxSum:
                maxSum = curSum
                ret = [start,i]

        return ret
