'''
Problem:

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

'''



'''
Solution: BFS

将wordDict中单词word的每一个字母使用下划线“_”代替，得到wordKey

可以构造wordKey -> word的映射，记为neighbors

在BFS的执行过程中，将当前单词word的每一位以下划线“*”代替，

在neighbors字典中查找其“相邻”单词（只改变一个字母得到的单词）

'''


from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def wordDiff(wordA, wordB):
            return sum([wordA[x] != wordB[x] for x in range(len(wordA))])
        
        visited = set([beginWord])
        q = deque()
        q.append((beginWord,1))
        neighbours = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                token = word[:i] + "*" + word[i+1:]
                neighbours[token].append(word)
        
        while len(q):
            curr, level = q.popleft()
            if wordDiff(curr, endWord) <= 1:
                return level+1    # count in the last word
            for i in range(len(curr)):
                token = curr[:i] + '*' + curr[i+1:]
                for nei in neighbours[token]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,level+1))
                        
        return 0
                        
                
