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

    
    
'''
Problem 3: 重复选择+最大价值

Given n kind of items with size Ai and value Vi( each item has an infinite number available) and a backpack with size m. 
What's the maximum value can you put into the backpack?
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPackIII(self, m, A, V):
        dp = [0] * (m+1)
        for i in range(len(A)):
            for j in range(1,m+1):
                if j - A[i] >= 0:
                    dp[j] = max(dp[j] , dp[j-A[i]] + V[i])
        return dp[m]

    
    
'''
Problem 4: 重复选择+唯一排列+装满可能性总数

Given n items with size nums[i] which an integer array and all positive numbers, no duplicates. 
An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may be chosen unlimited number of times
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPackIV(nums, target):
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(1,target+1):
                if nums[i] == j: 
                    dp[j] += 1
                elif j - nums[i] > 0:
                    dp[j] += dp[j-nums[i]]
        return dp[m]
    
    
