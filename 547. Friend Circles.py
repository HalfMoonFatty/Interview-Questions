'''
Problem:

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are 
direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
 
Output: 2

Explanation:
The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.


Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]

Output: 1

Explanation:
The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
'''


# Solution 1: Union Find

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        def findRoot(x):
            if x == unionSet[x]:
                return x
            unionSet[x] = findRoot(unionSet[x])
            return unionSet[x]
        
        
        def union(x, y):
            rootX = findRoot(x)
            rootY = findRoot(y)
            if rootX != rootY:
                unionSet[rootX] = rootY
            return
        
        
        unionSet = [i for i in range(len(M))]
        count = len(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]:
                    if findRoot(i) != findRoot(j):
                        union(i, j)
                        count -= 1
        return count
        
 
 
 # DFS: FloodFill 搜索
 
 class Solution(object):
    def findCircleNum(self, M):

        def dfs(i):
            for j in range(len(M)):
                if M[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        
        visited = [False] * len(M)
        count = 0
        for i in range(len(M)):
            if not visited[i]:
                dfs(i)
                count += 1
                
        return count
        
        
        
# BFS

import collections
class Solution(object):
    def findCircleNum(self, M):
        
        def bfs(i):
            q = collections.deque([i])
            while len(q):
                i = q.popleft()
                for j in range(len(M)):
                    if M[i][j] and not visited[j]:
                        visited[j] = True
                        q.append(j)
        
        
        visited = [False] * len(M)
        count = 0
        for i in range(len(M)):
            if not visited[i]:
                bfs(i)
                count += 1
                
        return count
        
        
        
