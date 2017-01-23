'''
Problem:

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. 
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

'''
Solution:

dp[i][x] 表示长度为 i 的subarray(nums[0] ~ nums[i-1]), Sum 为 x 的方法数

初始令dp[0][0] = 1

状态转移方程：
    dp[i + 1][k + nums[i]] += dp[i][k]
    dp[i + 1][k - nums[i]] += dp[i][k]

Note: i表示的是长度， 所以作为nums的下标需要-1

Time: O(m*n)
Space: O(m*n)
'''
   
class Solution(object):
    def findTargetSumWays(self, nums, S):

        dp = [collections.defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        
        for i in range(1,len(nums)+1):
            for k in dp[i-1].keys():
                dp[i][k+nums[i-1]] += dp[i-1][k]
                dp[i][k-nums[i-1]] += dp[i-1][k]
        return dp[-1][S]
 
 
 
# 利用滚动数组，可以将空间复杂度优化到O(n)，n为可能的运算结果的个数

class Solution(object):
    def findTargetSumWays(self, nums, S):

        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            ndp = collections.Counter()
            for sgn in (1, -1):
                for k in dp.keys():
                    ndp[k + n * sgn] += dp[k]
            dp = ndp
        return dp[S]
