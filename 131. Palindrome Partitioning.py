'''
Problem:

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
["aa","b"],
["a","a","b"]
]
'''

class Solution(object):
    def partition(self, s):

        def isValid(s,start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def getPart(s,start,res,results):
            if start > (len(s)-1):
                results.append(res[:])
            else:
                for i in range(start,len(s)):
                    if isValid(s,start,i):
                        res.append(s[start:i+1])
                        getPart(s,i+1,res[:],results)
                        res.pop()
            return results

        results = []
        return getPart(s,0,[],[])
