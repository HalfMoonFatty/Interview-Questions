'''
Problem:

Given a picture consisting of black and white pixels, and a positive integer N, 
find the number of black pixels located at some specific row R and column C that align with all the following rules:

- Row R and column C both contain exactly N black pixels.
- For all rows that have a black pixel at column C, they should be exactly the same as row R

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

Example:

Input:                                            
[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 

N = 3
Output: 6


Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index                                            
0    [['W', 'B', 'W', 'B', 'B', 'W'],    
1     ['W', 'B', 'W', 'B', 'B', 'W'],    
2     ['W', 'B', 'W', 'B', 'B', 'W'],    
3     ['W', 'W', 'B', 'W', 'B', 'W']]    
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.

Note: The range of width and height of the input 2D array is [1,200].

'''


'''
Solution:

利用数组rows，cols分别记录某行、某列'B'像素的个数。

然后利用字典sdict统计每一行像素出现的个数。 if sdict[row] != N: countinue

因为对于rule 2, 所有在某一column C有 "B" 的row必须看起来一模一样，
而条件 1 规定 column C contain exactly N black pixels. 所以一模一样的行数就是 column C 的 "B" 数(N)。

最后遍历一次picture即可。

Time complexity: O(m*n).
'''


class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        w, h = len(picture[0]), len(picture)
        rows, cols = [0] * h, [0] * w
        
        for x in range(h):
            for y in range(w):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1

        sdict = collections.defaultdict(int)
        for idx, row in enumerate(picture):
            sdict[''.join(row)] += 1

        ans = 0
        for x in range(h):
            row = ''.join(picture[x])
            if sdict[row] != N:
                continue
            for y in range(w):
                if picture[x][y] == 'B' and rows[x] == cols[y] == N:
                    ans += 1
        return ans
