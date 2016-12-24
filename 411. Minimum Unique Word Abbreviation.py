'''
Problem:

A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest 
possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Note:
In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
'''

'''
Solution: DFS + 剪枝

复用题目Valid Word Abbreviation的单词缩写检测方法validWordAbbreviation

首先将dictionary中长度与target不同的单词去掉。

DFS从空字符串''出发，逐一增加target中的字母；并尝试越过一些字母，插入数字。

遍历dictionary中的单词，检测冲突，若不存在冲突，则递归，并更新最优解。

剪枝策略：利用变量length记录当前时刻的最优的单词缩写长度，若DFS分支的长度大于length，则可剪枝。
'''

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """

        def validWordAbbreviation(word, abbr):
            size = len(word)
            cnt = loc = 0
            for w in abbr:
                if w.isdigit():
                    if w == '0' and cnt == 0:
                        return False
                    cnt = cnt * 10 + int(w)
                else:
                    loc += cnt
                    cnt = 0
                    if loc >= size or word[loc] != w:
                        return False
                    loc += 1
            return loc + cnt == size


        def dfs(target, index, length, abbr, result):
            if length >= self.minLength: return
            if index == len(target):
                for word in self.dlist:
                    if validWordAbbreviation(word, abbr):
                        return
                result[0] = abbr
                self.minLength = length
                return
            dfs(target, index + 1, length + 1, abbr + target[index], result)
            if index == 0 or not abbr[-1].isdigit():
                for x in range(2, len(target) - index + 1):
                    dfs(target, index + x, length + 1, abbr + str(x), result)


        self.dlist = [d for d in dictionary if len(d) == len(target)]
        self.minLength = len(target)
        result = [target]
        dfs(target, 0, 0, '', result)
        return result[0]
