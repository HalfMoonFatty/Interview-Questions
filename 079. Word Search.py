'''
Problem:

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, Given board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.
'''


class Solution(object):
    def exist(self, board, word):

        def dfsSearch(index, board, r, c, visited):
            if index == len(word):
                return True

            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or visited[r][c]:
                return False

            visited[r][c] = True
            char = board[r][c]
            if word[index] == board[r][c]:
                dir = ((0,1),(0,-1),(1,0),(-1,0))
                for d in dir:
                    if dfsSearch(index+1, board, r+d[0], c+d[1], visited):
                        return True
            visited[r][c] = False


        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if dfsSearch(0, board, i, j, visited):
                    return True
        return False
