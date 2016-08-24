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


class Solution:

    def minWindow(self, source, target):

        if (source =="" or target ==""):
            return ""

        # note tarmap and winmap have same set of keys
        tarmap= {}
        for c in target:
            tarmap[c] = tarmap.get(c, 0) + 1

        winmap = dict.fromkeys(target, 0)

        count = 0
        minLen = len(target)+1
        i, j = 0,0
        ans = ''

        while j < len(source):

            if winmap.has_key(source[j]):
                if winmap[source[j]] < tarmap[source[j]]:
                    count += 1
                winmap[source[j]] += 1


            if count == len(target):
                while i < j:
                    if winmap.has_key(source[i]):
                        if winmap[source[i]] == tarmap[source[i]]:
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
