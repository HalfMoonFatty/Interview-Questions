'''
Problem:

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as 
the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining 
elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. 
If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3

Note:
All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].

'''


'''
Solution:

首先将输入字符串列表strs按照长度递减排序，记得到的新列表为slist。

利用计数器cnt统计每个字符串出现的次数。

遍历slist，记当前字符串为c，其下标为i：

    若c在strs中出现不止一次，跳过该字符串

    否则，利用贪心算法对c和slist[0 .. i - 1]的字符串进行匹配，若均匹配失败，则返回len(c)

遍历结束，返回-1

'''


import collections
class Solution(object):
    def findLUSlength(self, strs):

        def isUncommon(pstr,cstr):
            pp = pc = 0
            while pp < len(pstr) and pc < len(cstr):
                if pstr[pp] == cstr[pc]:
                    pc += 1
                pp += 1
            return pc != len(cstr)

        
        cnt = collections.Counter(strs)
        slist = sorted(set(strs), key=len, reverse=True)
        
        for i in range(len(slist)):
            if cnt[slist[i]] > 1: 
                continue
            
            common = False
            for j in range(i):
                if not isUncommon(slist[j], slist[i]):
                    common = True
                    break
            if not common:
                return len(slist[i])
        return -1
            
