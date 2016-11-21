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
      
  
  
  
# Solution 2: 2 pointers

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
        
        for i in range(wordlen):
            word_map = {}
            finished = 0
            left = i

            for j in range(i,len(s)-wordlen+1,wordlen):
                curstr = s[j:j+wordlen]
                if word_count.has_key(curstr):
                    word_map[curstr] = word_map.get(curstr,0)+1
                    if word_map[curstr] <= word_count.get(curstr,0):
                        finished += 1
                    else:
                        while word_map[curstr] > word_count[curstr]:
                            word_map[s[left:left+wordlen]] -= 1
                            if word_map[s[left:left+wordlen]] < word_count[s[left:left+wordlen]]: 
                                finished -= 1
                            left += wordlen
 
                    if finished == n:
                        result.append(left)
                        word_map[s[left:left+wordlen]] -= 1
                        finished -= 1
                        left += wordlen
                
                else: 
                    word_map.clear()
                    finished = 0
                    left = j+wordlen

        return result 
                
