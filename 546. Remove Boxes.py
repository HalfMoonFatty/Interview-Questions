'''
Problem:

Given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes 
with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

Example 1:

Input: [1, 3, 2, 2, 2, 3, 4, 3, 1]

Output: 23

Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

Note: The number of boxes n would not exceed 100.

'''

'''
Solution:

First Attempt

The initial thought is straightforward, try every possible removal and recursively search the rest. No doubt it will be a TLE answer. 
Obviously there are a lot of recomputations involved here. Memoization is the key then. But how to design the memory is tricky. 


One step further

I think the problem of the approach above is that there are a lot of unnecessary computations (not recomputations). 
For example, if there is a formation of ABCDAA, we know the optimal way is B->C->D->AAA. 
On the other hand, if the formation is BCDAA, meaning we can't find an A before D, we will simply remove AA, which will be the optimal solution. 
Note this is true only if AA is at the end of the array. 
With naive memoization approach, the program will search a lot of unnecessary paths, such as C->B->D->AA, D->B->C->AA.

Now design cache[l][r][k]: the largest number we can get using lth to rth (inclusive) boxes with k same colored boxes as rth box appended at the end. 
Example, memo[l][r][3] represents the solution for this setting: [b_l, ..., b_r, A,A,A] with b_r == A. 
cache[l][r][k]表示第l到第r个合并后的盒子，连同其后颜色为color[r]的长度k一并消去所能得到的最大得分。

The transition function is to find the maximum among all b_i==b_r for i=l,...,r-1:

cache[l][r][k] = max(cache[l][r][k], memo[l][i][k+1] + memo[i+1][r-1][0])

Basically, if there is one i such that b_i == b_r, we partition the array into two: 

[b_l, ..., b_i, b_r, A, ..., A], and [b_{i+1}, ..., b_{r-1}]. 

The solution for first one will be memo[l][i][k+1], and the second will be memo[i+1][r-1][0]. 

Otherwise, we just remove the last k+1 boxes (including b_r) and search the best solution for lth to r-1th boxes. 
(One optimization here: make r as left as possible, this improved the running time from 250ms to 35ms)

The final solution is stored in memo[0][n-1][0] for sure.

'''

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def dfs(boxes, l, r, k, cache):
            if l > r: return 0
            if cache[l][r][k]: return cache[l][r][k]
            
            while l > r and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            cache[l][r][k] = dfs(boxes,l,r-1,0,cache) + (k+1)*(k+1)    # 首先把连续相同颜色的盒子进行合并。
            
            for i in range(l,r):
                if boxes[i] == boxes[r]:
                    cache[l][r][k] = max(cache[l][r][k], dfs(boxes, l, i, k+1, cache) + dfs(boxes, i+1, r-1, 0, cache))
            
            return cache[l][r][k]
            
        n = len(boxes)
        cache = [[[0] * n for i in range(n)] for j in range(n)]
        return dfs(boxes, 0, n-1, 0, cache)
        
