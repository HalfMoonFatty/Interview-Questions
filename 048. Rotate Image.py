'''
Problem:

    You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise).

Follow up:
    Could you do this in-place?

'''

'''
Solution:

Time: O(n^2)
Space: O(1)

'''

class Solution(object):

    def rotate(self, matrix):

        n = len(matrix)
        for layer in range(n/2):
            first = layer
            last = n-1-layer
            for i in range(first, last):
                offset = i - first
                tmp = matrix[first][i]
                # top <- left
                matrix[first][i] = matrix[last-offset][first]
                # left <- bottom
                matrix[last-offset][first] = matrix[last][last-offset]
                # bottom <- right
                matrix[last][last-offset] = matrix[i][last]
                # right <- top
                matrix[i][last] = tmp
        return
