'''
Problem:

    According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules :

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
    Could you solve it in-place? Remember that the board needs to be updated at the same time: 
    You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, 
    which would cause problems when the active area encroaches the border of the array. 
    How would you address these problems?
'''


'''
Solution:
    Since the board has ints but only the 1-bit is used, use the 2nd bit to store the new state. We cannot replace the old state directly by the new state.

    - Loop through every node on the matrix and count the live of the node's neightbours:
        if count == 3, no matter what the node's current status is (dead (0) or live(1))
        if count == 2, and current node is live(1) (since the board[i][j]'s 2nd bit hasn't been changed yet, so no need to mask)
        the new state is LIVE - set the 2nd bit to be 1

    - At the end, replace the old state with the new state by shifting all values one bit to the right.
'''


class Solution(object):
    def gameOfLife(self, board):
        """
            :type board: List[List[int]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
        def countLiveNeigh(i,j):
            count = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0<=x<len(board) and 0<=y<len(board[0]) and not(x == i and y == j):
                        count += board[x][y]&1    # mask all other bits except the last bit
            return count
   

        # Update state by counting neighbor cells
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = countLiveNeigh(i,j)
                if count == 3 or (count == 2 and board[i][j] == 1):   
                    # set the 2nd bit to 1(live) and keep the original state on 1st bit
                    board[i][j] |= 2    
   

        # replace the old state with the new state
        for i in range(len(board)):
            for j in range(len(board[0])):
                # replace the old state with the new state by shifting all values one bit to the right
                board[i][j] >>= 1       

        return



'''
Follow up:
In this question, we represent the board using a 2D array. 
In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. 
How would you address these problems?
'''

'''
Solution:
    - Transform the board to a set and Store the coordinates of all living cells in a set.
    - Then count the living neighbors of all cells by going through the living cells and increasing the counter of their neighbors.
    - Afterwards collect the new set of living cells by picking those with the right amount of neighbors.
'''


import collections
class Solution(object):
    def gameOfLife(self, board):

        def gameOfLifeInfinite(live):
            neighbors = collections.Counter()
            for i, j in live:
                for I in (i-1, i, i+1):
                    for J in (j-1, j, j+1):
                        if I != i or J != j:
                            neighbors[I, J] += 1
            new_live = set()
            for ij in neighbors.keys():
                if neighbors[ij] == 3 or neighbors[ij] == 2 and ij in live:
                    new_live.add(ij)
            return new_live
       
        # transform the board to a set and store the coordinates of all living cells in a set.
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
       
        live = gameOfLifeInfinite(live)
       
        # Afterwards collect the new set of living cells
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)
