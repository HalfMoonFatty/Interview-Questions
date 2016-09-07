'''
Problem:
   
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
   
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".

'''

# Solution 1 DP
class Solution(object):
    def wordBreak(self, s, wordDict):
       
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
       
        return dp[-1]
        
   
        
# Solution 2 Backtracking
class Solution(object):
    def wordBreak(self, s, wordDict):
       
        def dfs(start, s, wordDict):
            if start == len(s): return True
                
            for i in range(start+1,len(s)+1):
                if s[start:i] in wordDict:
                    if dfs(i,s,wordDict):
                        return True
                
            return False
       
        return dfs(0,s,wordDict)
