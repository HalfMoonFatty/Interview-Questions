'''
Problem:


Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. 

You may assume the following rules:
    You receive a valid board, made of only battleships or empty slots.
    Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column).
    At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.
'''


'''
Solution:

由于board中的战舰之间确保有'.'隔开，因此遍历board，若某单元格为'X'，只需判断其左边和上边的相邻单元格是否也是'X'。
如果左邻居或者上邻居单元格是'X'，则说明当前单元格是左边或者上边战舰的一部分；
否则，令计数器+1

Time: O(n^2)
Space: O(1)
'''

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board: return 0
        
        h, w = len(board), len(board[0])
        count = 0
        
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X' or j > 0 and board[i][j-1] == "X":
                        continue
                    count += 1
                
        return count 
