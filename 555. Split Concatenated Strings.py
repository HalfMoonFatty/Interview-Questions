'''
Problem:

Given a list of strings, you could assemble these strings together into a loop. Among all the possible loops, you need to find the 
lexicographically biggest string after cutting and making one breakpoint of the loop, which will make a looped string into a regular one.

So, to find the lexicographically biggest string, you need to experience two phases:

Assemble all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
Cut and make one breakpoint in any place of the loop, which will make a looped string into a regular str starting from the char at the cutting point.
And your job is to find the lexicographically biggest one among all the regular strings.

Example:
Input: "abc", "xyz"
Output: "zyxcba"
Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", where '-' represents the looped status. 
The answer string came from the third looped one, where you could cut from the middle and get "zyxcba".

Note:
The input strings will only contain lowercase letters.
The total length of all the strings will not over 1000.
'''

'''
Solution:

遍历strs中的字符串，若逆置后的字典序较大，则将其逆置

枚举字符串st，记下标为i，st左右两侧的字符串分别为left, right

在st中枚举起点j，则s[j:] + right + left + s[:j]为环形字符串从j处切割得到的新字符串

left + s[:j] + s[j:] + right ==> s[j:] + right + left + s[:j]

需要注意的是在枚举st时，需要同时判断st与st的逆置
'''

class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [max(s, s[::-1]) for s in strs]    # lexicographically biggest
        ans = ''
        for i, st in enumerate(strs):
            left, right = ''.join(strs[:i]), ''.join(strs[i+1:])
            for s in (st, st[::-1]):   # need to check both case for a word
                for j in range(len(s)):
                    ans = max(ans, s[j:] + right + left + s[:j])    # lexicographically biggest
        return ans
