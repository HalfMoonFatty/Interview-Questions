'''
Problem 1: 单次选择+最大体积

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Example

If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. 
If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.
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

Example

Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.
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

Example

Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
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
Problem 4: 单次选择+装满可能性总数   

Given n items with size nums[i] which an integer array and all positive numbers. 
An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may only be used once.

Example: Given candidate items [1,2,3,3,7] and target 7,

A solution set is:
[7]
[1, 3, 3]
return 2
'''

class Solution:
    def backPackIV(nums, target):
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(target,-1,-1):
                if j - nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]
        return dp[-1]
        

        
'''
Problem 5: 重复选择+唯一排列+装满可能性总数

Given n items with size nums[i] which an integer array and all positive numbers, no duplicates. 
An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may be chosen unlimited number of times
'''

class Solution:
    def backPackV(nums, target):
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(1,target+1):
                if nums[i] == j: 
                    dp[j] += 1
                elif j - nums[i] > 0:
                    dp[j] += dp[j-nums[i]]
        return dp[-1]
    
    
    
'''
Problem 6: 重复选择+不同排列+装满可能性总数

Given an integer array nums with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Note: The different sequences are counted as different combinations.

Example: Given nums = [1, 2, 4], target = 4

The possible combination ways are:
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[4]
return 6
'''

class Solution:
    def backPackVI(nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for j in range(1,target+1):
            for i in range(len(nums)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]
        return dp[-1]
            
