'''
Problem:

	Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. 
	If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. 
	After the burst, the left and right then becomes adjacent.

	Find the maximum coins you can collect by bursting the balloons wisely.

Note:
	(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
	(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:
    Given [3, 1, 5, 8], Return 167
    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''

'''
Solution: DP

- k -- Window size - 1
- left, right -- left and right boundaries
- last- last bursted balloon
- dp[left][right] -- within in range [left to right] max coins that I can get.
'''

class Solution(object):
    def maxCoins(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        if not nums: return 0
            
        nums = [n for n in nums if n > 0]    # remove '0'
        nums = [1] + nums + [1]  
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for k in range(2,n):
            for left in range(0,n-k):        
                right = left + k
                for last in range(left+1,right):    # last in [left+1,right-1]
                    dp[left][right] = max(dp[left][right], nums[left]*nums[last]*nums[right]+dp[left][last]+dp[last][right])

    	return dp[0][n-1]
