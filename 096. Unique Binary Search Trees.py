'''
Problem:

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

1            3     3      2      1
   \        /     /      / \      \
     3     2     1      1   3      2
   /     /         \                 \
 2      1           2                 3
'''

'''
Solution 1: Recursion (Calatan Number) - TLE 


|—————————------—-|———|-----------------------——————|
|                 | i |                             |
|—————————-------—|———|——————-----------------------|

|<—- i-1 nodes -—>|   |<——---—— n - i nodes ————--—>|

'''

class Solution:

    def numTrees(self, n):
        res = 0
        if n == 0:
            return 1
        for i in range(1,n+1):
            res += self.numTrees(i-1)*self.numTrees(n-i)
        return res




# Solution 2: DP

class Solution(object):
    def numTrees(self, n):

        G = [0]*(n+1)   # 0个...n个, n+1 cases
        G[0] = G[1] = 1

        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]
        return G[-1]


