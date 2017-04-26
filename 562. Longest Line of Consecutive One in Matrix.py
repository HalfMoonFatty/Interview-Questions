'''
Problem:

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]

Output: 3

Hint: The number of elements in the given matrix will not exceed 10,000.
'''

'''
Solution: DP

分表用二维数组h[x][y], v[x][y], d[x][y], a[x][y]表示以元素M[x][y]结尾，横向、纵向、主对角线、反对角线连续1的最大长度

状态转移方程如下：

h[x][y] = M[x][y] * (h[x - 1][y]  + 1)

v[x][y] = M[x][y] * (v[x][y - 1]  + 1)

d[x][y] = M[x][y] * (d[x - 1][y - 1]  + 1)

a[x][y] = M[x][y] * (a[x + 1][y - 1]  + 1)
'''

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        h, w = len(M), len(M) and len(M[0]) or 0
        ans = 0

        #horizontal & diagonal
        diag = [[0] * w for r in range(h)]
        for x in range(h):
            cnt = 0
            for y in range(w):
                cnt = M[x][y] * (cnt + 1)
                diag[x][y] = M[x][y]
                if x > 0 and y > 0 and M[x][y] and diag[x - 1][y - 1]:
                    diag[x][y] += diag[x - 1][y - 1]
                ans = max(ans, cnt, diag[x][y])

        #vertical & anti-diagonal
        adiag = [[0] * w for r in range(h)]
        for x in range(w):
            cnt = 0
            for y in range(h):
                cnt = M[y][x] * (cnt + 1)
                adiag[y][x] = M[y][x]
                if y < h - 1 and x > 0 and M[y][x] and adiag[y + 1][x - 1]:
                    adiag[y][x] += adiag[y + 1][x - 1]
                ans = max(ans, cnt, adiag[y][x])

        return ans
