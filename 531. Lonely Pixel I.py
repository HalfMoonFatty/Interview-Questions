'''
Problem:

Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:

Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3

Explanation: All the three 'B's are black lonely pixels.

Note: The range of width and height of the input 2D array is [1,500].
'''


'''
Solution:

利用数组rows，cols分别记录某行、某列'B'像素的个数。

然后遍历一次picture即可。

'''


