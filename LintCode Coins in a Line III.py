'''
Problem:

There are n coins with different value in a line. Two players take turns to take one coins from left side or right side until there are no more coins left. 
The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?
'''


'''
Solution:
state: 
	f[x][y] 现在还第x到第y的硬币,现在先手取硬币的人最后最多取硬币价值 

function:
	f[x][y] = max(min(f[x+2][y], f[x+1][y-1])+a[x]) , (min(f[x][y-2], f[x+1][y-1])+a[y])

intialize:
	f[x][x] = a[x]
	f[x][x+1] = max(a[x],a[x+1])
	
answer:
	f[0][n] > sum(a)/2

note: 
	f[x+2][y]:   后手拿x+1,先手拿x
	f[x+1][y-1]: 后手拿y,先手拿x
	f[x][y-2]:   后手拿y-1,先手拿y
	f[x+1][y-1]: 后手拿x,先手拿y
	f[x][y] = max(min(f[x+2][y], f[x+1][y-1])+a[x]) , (min(f[x][y-2], f[x+1][y-1])+a[y])
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
                a = dp[i+2][j] if i+2 < n else 0
                # dp[i+1][j-1]: player2: j,player1: i / player2: i,player1: j
                b = dp[i+1][j-1] if i+1 < n and j-1 >= 0 else 0
                # dp[i][j-2]: player2: j-1,player1: j
                c = dp[i][j-2] if j-2 >= 0 else 0
                dp[i][j] = max(min(a,b)+nums[i], min(b,c)+nums[j])

        return dp[0][-1] > sum(nums)/2
