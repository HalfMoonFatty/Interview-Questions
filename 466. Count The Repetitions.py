'''
Problem:

Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. 
For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. 
Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return: 2
'''


'''
Solution:

利用贪心算法计算s1与s2对应字符的匹配位置，由于s1与s2的循环匹配呈现周期性规律，因此可以通过辅助数组cache进行记录

记l1, l2为s1, s2的长度；i1, i2为s1, s2的字符下标, 令j1, j2 = i1 % l1, i2 % l2

当s1[i1] == s2[i2]时：

  若cache[j1][j2]不存在，则令cache[j1][j2] = i1, i2
  
  否则，记start1, start2 = dp[j1][j2]，循环节为s1[start1 ... i1], s2[start2 ... i2]


Example: 
s1="acb", n1=8
s2="abb", n2=2

     0  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2 
s1 = a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  
     0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23  Total Length = 3*8 = 24
     i1    i1       i1 i1
     
     
     0  1  2  0  1  2     
s2 = a  b  b  a  b  b    
     0  1  2  3  4  5    Total Length = 3*2 = 6
     i2 i2 i2 i2
     
     
i1 = 0, i2 = 0; j1 = 0%3 = 0  j2 = 0%3 = 0 ==> cache[0%3][0%3] = cache[0][0] = [0][0]
i1 = 2, i2 = 1; j1 = 2%3 = 2  j2 = 1%3 = 1 ==> cache[2%3][1%3] = cache[2][1] = [2][1]
i1 = 5, i2 = 2; j1 = 5%3 = 2  j2 = 2%3 = 2 ==> cache[5%3][2%3] = cache[2][2] = [5][2]

i1 = 6, i2 = 3; j1 = 6%3 = 0  j2 = 3%3 = 0 ==> cache[6%3][3%3] = cache[0][0] = [][]
i1 = 8, i2 = 4; j1 = 8%3 = 2  j2 = 4%3 = 2 ==> cache[8%3][4%3] = cache[2][1] = [][]
i1 = 11, i2 = 5; j1 = 11%3 = 2  j2 = 5%3 = 2 ==> cache[11%3][5%3] = cache[2][2] = [][]

When i = 6 we found the repetition (and stop counting on). 
nround = (3*8-0)/(6-0) = 4. 就是说一共有24个char长，可以包含4个长度为6的pattern ("acbacb").
对于 S2 而言长度为3的pattern ("abb"), 有4套，那么就是说由S1可以组成的有 3*4 = 12那么长.
但是真正的S2实际上是 abbabb 有(3*2)6个char那么长，一共可以从S1那里拿到 12个char，所以12/6 = 2。
'''


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not set(s2) <= set(s1):
            return 0
            
        l1, l2 = len(s1), len(s2)
        cache = collections.defaultdict(dict)
        i1 = i2 = 0
        while i1 < l1*n1:
            while s1[i1 % l1] != s2[i2 % l2]:
                i1 += 1
            if i1 >= l1*n1: break
            
            j1, j2 = i1%l1, i2%l2
            if j2 not in cache[j1]:
                cache[j1][j2] = i1, i2
                print i1,j1, i2, j2, cache
            else:
                start1, start2 = cache[j1][j2]
                nround = (l1*n1-start1) / (i1-start1)
                print nround
                i1 = start1 + nround * (i1 - start1)
                i2 = start2 + nround * (i2 - start2)
            if i1 < l1 * n1:
                i1 += 1
                i2 += 1
        return i2 / (n2 * l2)
