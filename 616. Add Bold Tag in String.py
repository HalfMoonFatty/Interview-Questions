'''
Problem:


Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. 
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
'''

'''
Solution: 朴素解法

时间复杂度O(n * m)，其中n为s的长度，m为dict中字符串长度之和

变量start， end记录当前需要加粗标记的子串起止下标，初始为-1

在s中枚举子串起点i，记当前字符为c

遍历dict，寻找与s[i:]匹配长度最长的子串，记其长度为nend

    若nend > 0：
    
        若start为-1，将其设为i
        
        将end更新为其与nend + i的较大值
    
    否则：
    
         若 i >= end > 0：将<b> + s[start:end] + </b>累加至答案，并将start与end重置为-1
         
         若start == -1：将c累加至答案

若start > -1：将<b> + s[start:end] + </b>累加至答案

'''


class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        start = end = -1
        ans = ''
        for i, c in enumerate(s):
            nend = 0
            for word in dict:
                if s[i:].startswith(word):
                    nend = max(nend, len(word))
            if nend:
                if start == -1: start = i
                end = max(end, nend + i)
                continue
            if i >= end:
                ans += '<b>' + s[start:end] + '</b>'
                start = end = -1
            if start == -1: ans += c
        if start > -1: ans += '<b>' + s[start:end] + '</b>'
        return ans
