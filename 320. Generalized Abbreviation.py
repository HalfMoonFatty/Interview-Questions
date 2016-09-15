'''
Problem:
    Write a function to generate the generalized abbreviations of a word.

Example:
    Given word = "word", return the following list (order does not matter):
    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
            :type word: str
            :rtype: List[str]
            """
        def genAbbr(start, word, res, result, prevNum):
            if start == len(word):
                result.append(''.join(res[:]))
                return

            genAbbr(start+1, word, res+str(word[start]), result, False)
            if not prevNum:
                for length in range(1,len(word)-start+1): # replace 0, 1, 2, 3...all
                    genAbbr(start+length, word, res+str(length), result, True)
            return


        result = []
        genAbbr(0, word, '', result, False)
        return result
