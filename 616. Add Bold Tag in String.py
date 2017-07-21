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
Solution:

Time complexity : O(l∗s∗x). Three nested loops are there to fill bold array.
Space complexity : O(s). res and bold size grows upto O(s).

nother idea could be to merge the process of identification of the substrings in s matching with the words in dict. 
To do so, we make use of an array bold for marking the positions of the substrings in s which are present in dict. 
A True value at bold[i] indicates that the current character is a part of the substring which is present in dict.

We identify the substrings in s by considering only substrings of "lengthd" for a dictionary word d. 
Whenver such a substring is found with its beginning index as i(and end index (i+lengthd−1)), we mark all such positions in bold as True.

Thus, in this way, whenever a overlapping or consecutive matching substrings exist in s, a continuous sequence of True values is present in bold. 
Keeping this idea in mind, we traverse over the string s and keep on putting the current character in the resultant string res. 
At every step, we also check if the bold array contains the beginning or end of a continuous sequence of True values. 
At the beginnning of such a sequence, we put an opening bold tag and then keep on putting the characters of s till we find a position 
corresponding to which the last sequence of continuous True values breaks(the first False value is found). We put a closing bold tag at such a position. 
After this, we again keep on putting the characters of s in res till we find the next True value and we keep on continuing the process in the same manner.
'''

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        # fill bold
        bold = [False] * len(s)
        for word in dict:
            for i in range(len(s)-len(word)+1):
                if s[i:i+len(word)] == word:
                        bold[i:i+len(word)] = [True] * len(word)

        # generate res according to bold
        res = ''
        i = 0
        while i < len(s):
            if bold[i]:
                res += '<b>'
                while i < len(s) and bold[i]:
                    res += s[i]
                    i += 1
                res += '</b>'
            else:
                res += s[i]
                i += 1

        return res


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
            if i >= end and start != -1:
                ans += '<b>' + s[start:end] + '</b>'
                start = end = -1
            if start == -1: ans += c
        if start > -1: ans += '<b>' + s[start:end] + '</b>'
        return ans
