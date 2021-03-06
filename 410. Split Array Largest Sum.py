'''
Problem:

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.

Note: Given m satisfies the following constraint: 1 ≤ m ≤ length(nums) ≤ 14,000.

Examples:
Input: nums = [7,2,5,10,8], m = 2
Output: 18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''


'''
Solution 1: Binary Search

Time: O(nlogn)
Space: O(1)

The answer is between maximum value of input array numbers and sum of those numbers. Use binary search to approach the correct answer. 
3.1 Cut the array from left.
3.2 Try our best to make sure that the sum of numbers between each two cuts (inclusive) is large enough but still less than mid.
3.3 We'll end up with two results: either we can divide the array into more than m subarrays or we cannot.
- If we can't, it means that the mid value we pick is too small because we've already tried our best to make sure each part holds as many non-negative numbers 
  as we can but we still have numbers left. So, it is impossible to cut the array into m parts and make sure each parts is no larger than mid. We should increase m. 
- If we can, it is either we successfully divide the array into m parts and the sum of each part is less than mid, or we used up all numbers before we reach m. 
  Both of them mean that we should lower mid because we need to find the minimum one.

https://discuss.leetcode.com/topic/61324/clear-explanation-8ms-binary-search-java/6

'''

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canPart(maxsum):
            npartition = 1
            sums = 0
            for n in nums:
                sums += n
                if sums > maxsum:
                    sums = n
                    npartition += 1
                    if npartition > m:
                        return False
            return True
                        
            
                
        l = nmax = max(nums)    
        r = nsum = sum(nums)
        
        while l <= r:
            mid = l+(r-l)/2
            if canPart(mid): 
                r = mid-1
            else:
                l = mid+1
        return l

      
      
      


'''
Solution 2: DP

This solution does not take advantage of the fact that the numbers are non-negative (except to break the inner loop early).
On the other hand, it can be used for the problem containing arbitrary numbers

- dp[j] is the solution for splitting subarray n[j]...n[L-1] into s parts.
- dp[i] is splitting subarray n[i]...n[L-1] into s+1 parts. dp[i] = min{ max(dp[s,j], n[i]+...+n[j-1]) }, i+1 <= j <= L-s




|<---------------- i --------------->|
0   i <---------- j -------------> maxLen   L-1
|_________________|__________________|_______|     
    |<--leftSum-->|<---- dp[j+1] ---->|     

val = max(leftSum,dp[j+1])
dp[i] = min(dp[i], val)



Time: O(n^2 * m)
Space: O(n)

https://discuss.leetcode.com/topic/61405/dp-java/3
'''

import sys
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            dp[i] = nums[i] + dp[i+1]
        
        for part in range(2, m+1):
            maxLen = len(nums) + 1 - part
            for i in range(maxLen):
                dp[i] = sys.maxint
                leftSum = 0
                for j in range(i,maxLen):
                    leftSum += nums[j]
                    if leftSum > dp[i]: break   # no better soluiton, stop search
                    val = max(leftSum,dp[j+1])
                    dp[i] = min(dp[i], val)
        return dp[0]
        
