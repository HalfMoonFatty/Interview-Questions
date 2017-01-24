'''
Problem:

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 
and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. 
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.


Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.


Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
'''


'''
Solution 1: Alpha-Beta搜索 + 记忆化

If we think from the prospective of one player, what he gains each time is a plus, while, what player2 gains is a minus. Eventually if player1's score > 0, he can win.

函数 restScore(nums)计算当前玩家从nums中可以获得的最大收益，当收益>=0时，此玩家获胜

if start == end, there is no other choice but have to select nums[start]
otherwise, this current player has 2 options:
    --> nums[s]-helper(nums,s+1,e): this player select the front item, leaving the other player a choice from s+1 to e
    --> nums[e]-helper(nums,s,e-1): this player select the tail item, leaving the other player a choice from s to e-1
Then take the max of these two options as this player's selection, return it.
'''

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def restScore(nums, start, end, cache):
            if not cache[start][end]: 
                if start == end: 
                    cache[start][end] = nums[start]
                else: 
                    cache[start][end] = max(nums[start] - restScore(nums, start+1, end, cache), nums[end] - restScore(nums, start, end-1, cache))
            return cache[start][end]
        
        cache = [[0] * len(nums) for _ in range(len(nums))]
        return restScore(nums, 0, len(nums)-1, cache) >= 0


    
    
    
'''
Solution 2: DP Refer to Lintcode: coins in a line

Time: O(n^2)
Space: O(n^2)
'''
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1: return True
    
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # dp[i+2][j]: player2: i+1, player1: i
                a = dp[i+2][j] if i+2 <= n-1 else 0
                # dp[i+1][j-1]: player2: j,player1: i / player2: i,player1: j
                b = dp[i+1][j-1] if i+1 <= n-1 and j-1 >= 0 else 0
                # dp[i][j-2]: player2: j-1,player1: j
                c = dp[i][j-2] if j-2 >= 0 else 0
                dp[i][j] = max(min(a,b)+nums[i], min(b,c)+nums[j])
        
        return dp[0][-1] > sum(nums)/2
