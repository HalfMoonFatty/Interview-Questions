'''
Problem:

Given a rows x cols screen and a sentence represented by a list of words, 
find how many times the given sentence can be fitted on the screen.

Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word won't exceed 10.
1 ≤ rows, cols ≤ 20,000.


Example 1:
Input: rows = 2, cols = 8, sentence = ["hello", "world"]
Output: 1

Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.


Example 2:
Input: rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
Output: 2

Explanation:
a-bcd- 
e-a---
bcd-e-


Example 3:
Input: rows = 8, cols = 5, sentence = ["I", "had", "apple", "pie"]
Output: 2

Explanation:
I-had
apple
pie-I
had--
apple
pie-I
had--
apple

'''




class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wcount = len(sentence)
        wlens = [len(word) for word in sentence]
        slen = sum(wlens) + wcount
        cache = dict()
        row_index = col_index = word_index = ans = 0

        while row_index < rows:
            if (col_index, word_index) in cache:
                row_index0, ans0 = cache[(col_index, word_index)]
                nround = (rows - row_index0) / (row_index - row_index0 + 1)
                ans = ans0 + nround * (ans - ans0)
                row_index = row_index0 + nround * (row_index - row_index0)
            else:
                cache[(col_index, word_index)] = row_index, ans


            scount = (cols - col_index) / slen
            ans += scount
            col_index += scount * slen + wlens[word_index]

            if col_index <= cols:
                word_index += 1
                col_index += 1
                if word_index == wcount:
                    word_index = 0
                    ans += 1
            if col_index >= cols:
                col_index = 0
                row_index += 1
        return ans
