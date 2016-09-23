'''
Problem:

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9]. (order does not matter).

'''



# Solution 1

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n, wordlen = len(words), len(words[0])
        if not words or n*wordlen > len(s): return []
        
        result = []
        word_count = collections.Counter(words)

        for i in range(len(s) - n*wordlen+1):
            word_map = {}
            extraword = False
            for j in range(i,i+n*wordlen,wordlen):
                curstr = s[j:j+wordlen]
                word_map[curstr] = word_map.get(curstr,0)+1
                if word_map[curstr] > word_count.get(curstr,0):
                    extraword = True
                    break
            
            if not extraword:
                result.append(i)
        return result 
      
  
  
# Solution 2:

      
