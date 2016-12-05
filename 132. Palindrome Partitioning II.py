'''
Problem:

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''

'''
Solution 1:

Calculate and maintain 2 DP states:
- pal[i][j] , which is whether s[i..j] forms a pal
- minCuts[i], which is the minCut for s[i..n-1]; minCuts[0] initially sets to -1, which is needed in the case that s[0..i-1] is a palindrome.

if s[i..j] is a palindrome, then minCuts[j+1] will be updated to the minimum of the current minCuts[j+1] and minCut[i]+1
(i.e. cut s[0..j] into s[0,i-1] and s[i,j]).

Time:  O(N^2)
Space: O(N^2)
'''

class Solution(object):
    def minCut(self, s):
        """
            :type s: str
            :rtype: int
            """
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        minCuts = [0]*(n+1)
        for i in range(n+1): minCuts[i] = i-1

        for i in range(1,n+1):
            for j in range(i-1,-1,-1):
                if s[j] == s[i-1] and (i-1-j<2 or isPal[j+1][i-2]):
                    isPal[j][i-1] = True
                    minCuts[i] = min(minCuts[i], 1 + minCuts[j])

        return minCuts[-1]




'''
Solution 2: Optimized DP

minCUTS[i] is used to save the minimum cuts for s[0:i-1]. 
For each i, we do two for loops (for j loop) to check if the substrings s[i-j .. i+j] (odd-length substring) and s[i-j-1.. i+j] (even-length substring) are palindrome. 
By increasing j from 0, we can find all the palindrome sub-strings centered at i and update minCUTS accordingly. 
Once we meet one non-palindrome sub-string, we stop for-j loop since we know there no further palindrome substring centered at i. 
'''

class Solution(object):
    def minCut(self, s):
        """
            :type s: str
            :rtype: int
            """
        n = len(s)
        cnt = [0]*(n+1)
        for length in range(n+1):
            cnt[length] = length-1

        for c in range(n):
            # odd length palindrome
            r1 = 0
            while r1 <= c and c+r1 < n and s[c-r1] == s[c+r1]: # note for s r-c and r+c are indexes
                cnt[c+r1+1] = min(cnt[c-r1]+1, cnt[c+r1+1])
                r1 += 1
            # even length palindrome
            r2 = 1
            while r2-1 <= c and c+r2 < n and s[c-r2+1] == s[c+r2]:
                cnt[c+r2+1] = min(cnt[c-r2+1]+1, cnt[c+r2+1])
                r2 += 1
        return cnt[-1]
