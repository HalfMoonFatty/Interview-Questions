'''
Problem:

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note: The total number of elements of the given matrix will not exceed 10,000.

'''


'''
Solution:

初始对角线方向为右上方（偏移量：行-1, 列+1），遇到边界时转向左下方（偏移量：行+1, 列-1）

对于边界的处理：

向右上方移动遇到上边界时，若未达到右边界，则向右移动（偏移量：行+0，列+1），否则向下移动（偏移量：行+1，列+0）

向左下方移动遇到左边界时，若未达到下边界，则向下移动（偏移量：行+1，列+0），否则向右移动（偏移量：行+0，列+1）

'''


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        
        i, j, k = 0, 0, 1
        h, w = len(matrix), len(matrix[0])
        result = []
        
        for x in range(w * h):
            result.append(matrix[i][j])
            if k > 0:
                ni, nj = i - 1, j + 1
            else:
                ni, nj = i + 1, j - 1
                
            if 0 <= ni < h and 0 <= nj < w:
                i, j = ni, nj
            else:
                if k > 0:
                    if j + 1 < w:
                        j += 1
                    else:
                        i += 1
                else:
                    if i + 1 < h:
                        i += 1
                    else:
                        j += 1
                k *= -1
        return result
