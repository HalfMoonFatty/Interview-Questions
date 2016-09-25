'''
Problem:

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
     You may assume word1 and word2 are both in the list.
'''

'''
Solution:
    ind1 and ind2 are the indexes where word1 and word2 were last seen.
    Except if they're the same word, then i1 is the previous index.
'''

import sys
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
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
            if w == word1:
                ind1 = i
            # if not elif, so will enter both clause
            if w == word2:
                # if they're the same word,then ind1 is the previous index (ind2).
                if word1 == word2:
                    ind1 = ind2
                ind2 = i    # ind2 is new
            if ind1 != -1 and ind2 != -1:
                minDis = min(minDis, abs(ind1 - ind2))
        return minDis
