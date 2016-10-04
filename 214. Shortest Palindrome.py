'''
Problem:

    Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
    Find and return the shortest palindrome you can find by performing this transformation.

For example:
    Given "aacecaaa", return "aaacecaaa".
    Given "abcd", return "dcbabcd".

'''

'''
Solution : KMP + trick

The problem is same as "find the longest palindrome substring starts from 0". 

The trick is to build a temp string like this: s + "#" + reverse(s). We add "#" here to force the match in reverse(s) starts from its first index. 
What we do in KMP here is trying to find a match between prefix in s and a postfix in reverse(s). The match part will be palindrome substring (the value in last cell will be our solution). 
In this problem, we don't need to use KMP to match strings but instead we use the lookup table in KMP to find the palindrome.

'''

class Solution(object):
    def shortestPalindrome(self, s):

        def getLPS(tmp):
            length = 0
            lps = [0]*len(tmp)
            i = 1
            while i < len(tmp):
                if tmp[length] == tmp[i]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length > 0:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps


        tmp = s + "#" + s[::-1]
        lps = getLPS(tmp)
        return s[len(s)-1:lps[-1]-1:-1] + s
        
        
        
'''
Solution 2: TLE in python

The idea is to find the longest palindromic substring of s that begins with s[0]. Then take the remaining susbtring, reverse it and append it to the beginning of s.

The most difficult part is to implement the Manacher's algorithm to find the longest palindromic substring starting with s[0].

index    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
string   #  a  #  a  #  c  #  e  #  c  #  a  #  a  #  a  #
dp[]     0, 1, 2, 1, 0, 1, 0, 7, 0, 1, 0, 1, 2, 3, 2, 1, 0

Here we have 'e' is the first whose index == dp[i], we know that in the ORIGINAL string "aacecaaa", the length of longest palindrom starts with s[0] is (center/2)*2 = (7/2)*2 = 6; We need to reverse the string after index=5 and append it to the start of the original string: s[len(s)-1:center-1:-1] + s

'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
            :type s: str
            :rtype: str
            """
        t = '#'
        for i in range(len(s)):
            t += s[i]
            t += '#'

        dp = [0]*len(t)
        C = R = 0
        center = 0
        for i in range(1,len(dp)-1):
            mirror_i = 2*C-i
            if i < R:
                dp[i] = min(dp[mirror_i],R-i)
            else:
                dp[i] = 0

            # try to expand:
            while i+dp[i]+1<= len(dp)-1 and i-dp[i]-1 >= 0 and t[i+dp[i]+1] == t[i-dp[i]-1]:
                dp[i] += 1

            # realocate center:
            if dp[i] > R:
                C = i
                R = i+dp[i]

            # find the longest palindrom starts with s[0]
            # center = 4 ==> the length of the palin is 4
            if i == dp[i]:
                center = max(center,i)

        return s[len(s)-1:center-1:-1] + s
