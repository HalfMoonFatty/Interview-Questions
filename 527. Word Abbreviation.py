'''
Problem:

Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character 
until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.


Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.

'''


'''
Solution:

利用字典 result 维护原始字符串word到压缩字符串abbr的映射

尝试将所有字符串从最短长度开始进行压缩

若同一个压缩字符串对应多个原串，则将这些串递归求解

否则，将该压缩串的结果加入 result
'''

import collections
class Solution(object):


    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """

        def getAbbr(word, size):
            if len(word) - size <= 3: return word
            return word[:size + 1] + str(len(word) - size - 2) + word[-1]


        def solve(dict, size):
            dlist = collections.defaultdict(list)
            for word in dict:
                dlist[getAbbr(word, size)].append(word)

            for abbr, wlist in dlist.iteritems():
                if len(wlist) == 1:
                    self.result[wlist[0]] = abbr
                else:
                    solve(wlist, size + 1)


        self.result = {}
        solve(dict, 0)
        return self.result.values()
