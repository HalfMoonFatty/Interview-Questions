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

https://discuss.leetcode.com/topic/61405/dp-java/3
'''

        
