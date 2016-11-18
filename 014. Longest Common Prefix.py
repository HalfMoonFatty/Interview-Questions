'''
Problem:

    Write a function to find the longest common prefix string amongst an array of strings.

'''

'''
Solution:

Time complexity : O(S) , where S is the sum of all characters in all strings. In the worst case there will be n equal strings with length 
m and the algorithm performs S=m∗n character comparisons. In the best case there are at most n∗minLen comparisons where minLen is the length of the shortest string in the array.

Space complexity : O(1). We only used constant extra space.

'''

class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''

        prefix = ''
        for i in range(len(strs[0])):   # Use the first string as the standard
            for j in range(1,len(strs)):    # Check the rest of the strings;
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix
        

# Follow-up: trie
# https://leetcode.com/articles/longest-common-prefix/
        
