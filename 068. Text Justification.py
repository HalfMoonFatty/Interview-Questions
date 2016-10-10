'''
Problem:
   
    Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
   
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
   
    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
   
    For the last line of text, it should be left justified and no extra space is inserted between words.
  
For example,
    words: ["This", "is", "an", "example", "of", "text", "justification."]
    L: 16.
   
    Return the formatted lines as:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]
   

Note:
    Each word is guaranteed not to exceed L in length.
    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
'''



class Solution(object):
    def fullJustify(self, words, maxWidth):
 
        ret = []
        start = 0
        while start < len(words):
            # step1. find number of word to fit in this line
            nchars = 0
            nwordInLine = 0   
            while start+nwordInLine<len(words) and nchars+len(words[start+nwordInLine]) <= maxWidth-nwordInLine:
                nchars += len(words[start+nwordInLine])
                nwordInLine += 1
           
            # step2. padding:
            line = ''
            nspace = maxWidth - nchars
            ninsertion = nwordInLine-1
            
            line += words[start]
            for j in range(nwordInLine-1):    # nwordInLine-1 paddings 
                # case1: last line - add ONE space
                if start + nwordInLine > len(words)-1: 
                    line += ' '               
                else:
                    line += ' '*(nspace/ninsertion)
                    if j < nspace%ninsertion: # case2: uneven case
                        line += ' '
                line += words[start+j+1]
                
            # case3: <= 1 word in a line    
            line += ' '*(maxWidth-len(line))
            ret.append(line)
           
            start += nwordInLine
        return ret
