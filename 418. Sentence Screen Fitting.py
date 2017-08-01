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


'''
Solution:

Say sentence=["abc", "de", "f], rows=4, and cols=6.
The screen should look like

"abc de"
"f abc "
"de f  "
"abc de"
Consider the following repeating sentence string, with positions of the start character of each row on the screen.

"abc de f abc de f abc de f ..."
 ^      ^     ^    ^      ^
 0      7     13   18     25
Our goal is to find the start position of the row next to the last row on the screen, which is 25 here. Since actually it's the length of everything earlier, we can get the answer by dividing this number by the length of (non-repeated) sentence string. Note that the non-repeated sentence string has a space at the end; it is "abc de f " in this example.

Here is how we find that position. In each iteration, we need to adjust start based on spaces either added or removed.

"abc de f abc de f abc de f ..." // start=0
 012345                          // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
        012345                   // start=7+6+0=13
              012345             // start=13+6-1=18 (1 space added)
                   012345        // start=18+6+1=25 (1 space added)
                          012345
'''

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        start = 0
        length = len(s)
        for i in range(rows):
            start += cols
            # skip the last space
            if s[start % length] == ' ':
                start += 1
            # current word cannot fit in this row
            else:
                while start - 1 >= 0 and s[(start-1) % length] != ' ':
                    start -= 1
            
                    
        return start/length
                
            


'''
Solution:

由于rows和cols的规模可以达到20000，因此朴素的解法会超时（Time Limit Exceeded）

观察测试用例3可以发现，当句子在屏幕上重复展现时，会呈现周期性的规律

上例中apple单词的相对位置从第二行开始循环，因此只需要找到单词相对位置的“循环节”，即可将问题简化。

利用字典dp记录循环节的起始位置，具体记录方式为：cache[(col_index, word_index)] = row_index, ans

以数对(col_index, word_index)为键，其中 word_index 为单词在句子中出现时的下标，col_index 为单词出现在屏幕上的列数

以数对(row_index, ans)为值，其中 row_index 为单词出现在屏幕上的行数，ans为此时已经出现过的完整句子数

code 分为上下两部分：

第一部分用来确定 row_index 和 ans 或者把当前的 row_index 和 ans 写到 Cache 里
第二部分用来 col_index, row_index and word_index
    先计算 col_index (col_index += scount * slen + wlens[word_index])
    然后根据 col_index 的值 分两种情况讨论：
    * if col_index <= cols:
    * if col_index >= cols: 
        when current word exceed the screen boundry, need to move to the next new line 
        and without increment to the next word(word_index)        
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

            # if one line can fit in multiple words
            scount = (cols - col_index) / slen
            ans += scount
            col_index += scount * slen + wlens[word_index]

            if col_index <= cols:
                word_index += 1
                col_index += 1
                if word_index == wcount:
                    word_index = 0
                    ans += 1
            # when current word exceed the screen boundry, need to move to the next new line 
            # without increment to the next word(word_index) 
            if col_index >= cols:
                col_index = 0
                row_index += 1
        return ans
