'''
Problem:

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"

Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''


'''
Solution:

If the final answer has the same number of digits as the input string S, then the answer must be the middle digits + (-1, 0, or 1) flipped 
into a palindrome. For example, 23456 had middle part 234, and 233, 234, 235 flipped into a palindrome yields 23332, 23432, 23532. 
Given that we know the number of digits, the prefix 235 (for example) uniquely determines the corresponding palindrome 23532, 
so all palindromes with larger prefix like 23732 are strictly farther away from S than 23532 >= S.

If the final answer has a different number of digits, it must be of the form 999....999 or 1000...0001, as any palindrome smaller than 
99....99 or bigger than 100....001 will be farther away from S.


记n的前半部分为p，分别用p，p - 1，p + 1及其逆序串拼接成长度为奇数或者偶数的回文串。

假设n的长度为m， p的长度应分别取m / 2，m / 2 + 1。

另外需要考虑进位时的边界情况，比如测试用例：11, 1001, 999
'''


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        def genPals(sp):
            evenPal = int(sp + sp[::-1])
            oddPal = int(sp + sp[::-1][1:])
            return evenPal,oddPal
            
        
        if len(n) == 1: return str(int(n) - 1)
        
        s, n = n, int(n)
        ans = -999999999999999999
        mid = len(s) / 2
        
        for prefix in int(s[:mid]), int(s[:mid + 1]), int(s[:mid]) * 10:
            for d in -1, 0, 1:
                for pal in genPals(str(prefix + d)):
                    val = int(pal)
                    if val == n: continue
                    ans = min(ans, val, key = lambda x : (abs(x - n), x))
        return str(ans)
