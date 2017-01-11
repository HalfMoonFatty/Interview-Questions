'''
Problem:

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. 
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. 
In this scenario, how would you change your code?

'''


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        q = collections.deque(s)
        for char in t:
            if len(q) and char == q[0]:
                q.popleft()
        return len(q) == 0
            

        
'''
Use 2 pointers:
'''
class Solution(object):
    def isSubsequence(self, s, t):

        if not s: return True
        if not t: return False
        
        i = 0
        for char in s:
            i = t.find(char, i)
            if i < 0: return False
            i += 1
        return True
    
    
'''
Follow-up:
https://discuss.leetcode.com/topic/60134/java-code-for-the-problem-two-pointer-and-the-follow-up-binary-search
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # binary search to find the first index that is larger than current index
        def getNextIndex(index_list, index):
            if not index_list : return -1
            
            left, right = 0, len(index_list)-1
            while left < right:
                mid = left + (right-left)/2
                if index_list[mid] <= index: left = mid+1
                else: right = mid
                
            return index_list[left] if index_list[left] > index else -1
            
            
        
        index_map = collections.defaultdict(list)
        for i in range(len(t)):
            index_map[t[i]].append(i)
        
        index = -1
        for char in s:
            nextIndex = getNextIndex(index_map[char], index)
            if nextIndex < 0: return False
            index = nextIndex
        return True
        
