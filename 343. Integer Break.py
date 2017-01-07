'''
Problem:

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note:
     You may assume that n is not less than 2.

Hint:
There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

'''
class Solution(object):
    def integerBreak(self, n):
        """
            :type n: int
            :rtype: int
            """
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(j,dp[j])*max(i-j, dp[i-j]))
        return dp[-1]
        
'''        
Math solution

1. The factor can only be 2 or 3:
    If an optimal product contains a factor f >= 4, then you can replace it with factors 2 and f-2 without losing optimality, 
    as 2*(f-2) = 2f-4 >= f. So you never need a factor greater than or equal to 4, meaning you only need factors 1, 2 and 3 
    (and 1 is of course wasteful and you'd only use it for n=2 and n=3, where it's needed).

2. The max product of any n>4 must contain a factor of 3:
    - Out of 1, 2, 3, we know when n>4, if n is an odd number, 3 must be there as a factor (2 and 4 can't add up to an odd number);
    - Now say n is an even number (n>4) and only has factor of 2 and 4, we can always split a 6 to 3X3, which is better than 2X2X2.
    Therefore, the max product of any n (n>4) must contain a factor of 3. The recurrence relation holds.
'''

class Solution(object):
    def integerBreak(self, n):

        return 1 if n <= 2
        return 2 if n == 3
        return 4 if n == 4

        dp = [0] * (n+1)
        dp[2],dp[3], dp[4]= 2,3,4

        for i in range(5,n+1):
            dp[i] = 3 * dp[i-3]
        return dp[-1]
