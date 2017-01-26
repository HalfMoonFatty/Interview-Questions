'''
Problem 1: 单次选择+最大体积

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        dp = [0] * (m+1)
        for i in range(len(A)):
            for j in range(m,-1,-1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]] + A[i])
        return dp[m]    
    
    
'''
Problem 2: 单次选择+最大价值

Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPackII(self, m, A, V):
        dp = [0] * (m+1)
        for i in range(len(A)):
            for j in range(m, -1, -1):
                if j - A[i] >= 0:
                    dp[j] = max(dp[j] , dp[j-A[i]] + V[i])
        return dp[m]
