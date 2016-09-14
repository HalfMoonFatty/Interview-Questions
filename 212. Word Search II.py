'''
problem:

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

For example, Given words = ["oath","pea","eat","rain"] and

board =
[
['o','a','a','n'],
['e','t','a','e'],
['i','h','k','r'],
['i','f','l','v']
]
Return ["eat","oath"].

Note:

	You may assume that all inputs are consist of lowercase letters a-z.
	You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
	If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. 
	What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? 
	If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

'''


class Solution(object):
    def findWords(self, board, words):

        def dfsSearch(trie, r, c, string, results):
            # boundary or visited
            if r>len(board)-1 or c>len(board[0])-1 or r<0 or c<0 or visited[r][c]:
                return

            # check trie
            cur = board[r][c]
            if not trie.children.has_key(cur):
                return
            if trie.children[cur].isWord:
                results.add(string+cur)
                
            visited[r][c] = True
            dfsSearch(trie.children[cur], r-1, c, string+cur, results)
            dfsSearch(trie.children[cur], r+1, c, string+cur, results)
            dfsSearch(trie.children[cur], r, c-1, string+cur, results)
            dfsSearch(trie.children[cur], r, c+1, string+cur, results)
            visited[r][c] = False
            return


        # build a trie
        trie = Trie()
        for word in words:
            trie.addWord(word)

        results = set()
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfsSearch(trie.root, i, j, '', results)
        return list(results)
