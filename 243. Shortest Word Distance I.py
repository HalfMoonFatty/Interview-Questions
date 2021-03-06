'''
Problem:

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
     You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

'''



import sys
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
        ind1 = -1
        ind2 = -1
        minDis = sys.maxint
        for i,w in enumerate(words):
            # build up index map
            if w == word1:
                ind1 = i
            elif w == word2:
                ind2 = i
            # update the word distance
            if ind1 != -1 and ind2 != -1:
                minDis = min(minDis, abs(ind1 - ind2))
        return minDis
