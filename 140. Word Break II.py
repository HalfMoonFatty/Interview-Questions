'''
Problem:

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

# Solution 1: DFS+ Cache

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s, wordDict, cache):
            if cache.has_key(s): return cache[s]
            if len(s) <=0: return []
            
            result = []
            for length in range(1,len(s)+1):
                word = s[0:length]
                if word in wordDict:
                    if length == len(s): 
                        result.append(word)
                    else:
                        ret = dfs(s[length:], wordDict, cache)
                        for item in ret:
                            result.append(word + " " + item)
                            
            cache[s] = result
            return result
            
        return dfs(s, wordDict, {})




# Solution 2
class Solution(object):
   
    def wordBreak(self, s, wordDict):
       
        def dfs(s, wordDict, cache):
            if cache.has_key(s): return cache[s]
            if len(s) == 0: return []
            
            result = []
            for word in wordDict:
                if s.startswith(word):
                    if s == word:
                        result.append(word)
                    else:
                        ret = dfs(s[len(word):],wordDict,cache)
                        for r in ret:
                            result.append(word + " " + r)
            cache[s] = result
            return result
        
        cache = {}
        return dfs(s,wordDict,cache)
