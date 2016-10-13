'''
Problems:

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

'''

'''
Solution:

Idea is straightforward: get each pair of (i, j) and calculate length(word[i]) * length(word[j]) update the maximum answer.

Problem now becomes how to efficient check whether two words share common letter. Use a boolean[26], we can do this in linear time. However bit manipulation can reduce this to O(1) with preprocess.

Since the alphabet is only 26 therefore we can use one 32bit integer to represent the character occurrence then check if two word share common letter becomes check if bitwise and of the two integers is zero.


Time: O(n^2)??
Space: O(n)
'''

class Solution(object):
    def maxProduct(self, words):
        """
            :type words: List[str]
            :rtype: int
            """

        # build an array of mask
        masks = [0]*len(words)
        for i in range(len(words)):
            for char in words[i]:
                masks[i] |= 1 << (ord(char) - ord('a'))

        # calculate max Length
        maxLen = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if masks[i] & masks[j] == 0:
                    maxLen = max(maxLen, len(words[i])*len(words[j]))
        return maxLen
