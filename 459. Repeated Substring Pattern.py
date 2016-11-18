'''
Problem:

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.


Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

# 时间复杂度 O(k * n)，其中n是字符串长度，k是n的约数个数

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        for x in range(1, size / 2 + 1):
            if size % x:
                continue
            if str[:x] * (size / x) == str:
                return True
        return False
