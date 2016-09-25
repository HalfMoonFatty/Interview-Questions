'''
Problem:

    This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. 
    How would you optimize it?

    Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

    For example,
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    Given word1 = “coding”, word2 = “practice”, return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


# Solution: Pay attention to index iteration: if index1 < index2, increase index1; else increase index2.

import sys
from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
            initialize your data structure here.
            :type words: List[str]
            """
        self.indexmp = defaultdict(list)
        for i,w in enumerate(words):
            self.indexmp[w].append(i)


    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.indexmp[word1]
        l2 = self.indexmp[word2]
        minDis = sys.maxint
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            index1,index2 = l1[i],l2[j]
            if index1 < index2:
                minDis = min(minDis,index2 - index1)
                i += 1
            else:
                minDis = min(minDis,index1 - index2)
                j += 1
        return minDis


