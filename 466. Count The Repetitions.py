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
  
  否则，记start1, start2 = dp[j1][j2]，循环节为s1[start1 ... x1], s2[start2 ... x2]


Example: 
s1="acb", n1=8
s2="abb", n2=2

     0  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2 
s1 = a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  a  c  b  
     0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23  Total Length = 3*8 = 24
     i1    i1       i1
     
     
     0  1  2  0  1  2     
s2 = a  b  b  a  b  b    
     0  1  2  3  4  5    Total Length = 3*2 = 6
     i2 i2 i2
     
     
i1 = 0, i2 = 0; j1 = 0%3 = 0  j2 = 0%3 = 0 ==> cache[0%3][0%3] = cache[0][0] = [0][0]
i1 = 2, i2 = 1; j1 = 2%3 = 2  j2 = 1%3 = 1 ==> cache[2%3][1%3] = cache[2][1] = [2][1]
i1 = 5, i2 = 2; j1 = 5%3 = 2  j2 = 2%3 = 2 ==> cache[5%3][2%3] = cache[2][2] = [5][2]

i1 = 0, i2 = 0; j1 = 0%3 = 0  j2 = 0%3 = 0 ==> cache[0%3][0%3] = cache[0][0] = [0][0]
'''
