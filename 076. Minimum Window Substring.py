'''
Problem:

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

     For example,
     S = "ADOBECODEBANC"
     T = "ABC"
     Minimum window is "BANC".

Note:
	If there is no such window in S that covers all characters in T, return the empty string "".
	If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''


from collections import Counter
class Solution:

    def minWindow(self, source, target):
        
      if (source =="" or target ==""):
        return ""
        
        tarmap = Counter(target)
        winmap = dict.fromkeys(target, 0)
        count = 0
        i = j = 0
        ans = ''
        
        while j < len(source):    # 快
            if winmap.has_key(source[j]):
                if winmap[source[j]] < tarmap[source[j]]:
                    count += 1
                winmap[source[j]] += 1
                
            if count == len(target):
                while i < j:      # 慢
                    if winmap.has_key(source[i]):
                        if winmap[source[i]]-1 < tarmap[source[i]]:
                            break
                        winmap[source[i]] -= 1
                    i += 1
            
                if ans == '' or j-i < len(ans):
                    ans = source[i:j+1]
                    
                winmap[source[i]] -= 1
                count -= 1
                i += 1
            j += 1
        return ans
                    
