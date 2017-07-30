'''
Problems:

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. 
On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. 
Each 0 and 1 can be used at most once.

Note:
    The given numbers of 0s and 1s will both not exceed 100
    The size of given string array won't exceed 600.

Example 1:
    Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
    Output: 4
    Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
    
Example 2:
    Input: Array = {"10", "0", "1"}, m = 1, n = 1
    Output: 2
    Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
'''


'''
Solution: DP - 二维01背包问题（Knapsack Problem）


This problem can be solved by using 2-D Dynamic Programming. We can make use of a dp array, such that an entry dp[i][j] denotes 
the maximum number of strings that can be included in the subset given only i 0's and j 1's are available.

Now, let's look at the process by which we'll fill the dp array. We traverse the given list of strings one by one. 
Suppose, at some point, we pick up any string sk consisting of x zeroes and y ones. Now, choosing to put this string in any of the subset 
possible by using the previous strings traversed so far will impact the element denoted by dp[i][j] for i and j satisfying x ≤ i ≤ m, y ≤ j ≤ n. This is because for entries 
dp[i][j] with i < x or j < y, there won't be sufficient number of 1's and 0's available to accomodate the current string in any subset.

Thus, for every string encountered, we need to appropriately update the dp entries within the correct range.

Further, while updating the dp values, if we consider choosing the current string to be a part of the subset, 
the updated result will depend on whether it is profitable to include the current string in any subset or not. 
If included in the subset, the dp[i][j] entry needs to be updated as dp[i][j]=1+dp[i−zeroes_current_string][j−ones_current_string], 
where the factor of +1 takes into account the number of elements in the current subset being increased due to a new entry.

But, it could be possible that the current string could be so long that it could be profitable not to include it in any of the subsets. 
Thus, the correct equation for dp updation becomes:dp[i][j]=max(1+dp[i−zeroes_current_string][j−ones_current_string],dp[i][j])

Thus, after the complete list of strings has been traversed, dp[m][n] gives the required size of the largest subset.


状态转移方程：

for s in strs:
    zero, one = s.count('0'), s.count('1')
    for x in range(m, zero - 1, -1):
        for y in range(n, one - 1, -1):
            dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])

'''


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for x in range(m + 1)]
        for s in strs:
            zero, one = s.count('0'), s.count('1')
            for x in range(m, zero - 1, -1):
                for y in range(n, one - 1, -1):
                    dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
        return dp[m][n]
