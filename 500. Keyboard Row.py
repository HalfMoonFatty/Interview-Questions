'''
Problem:

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''



class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words: return []
        
        row = {1:'qwertyuiop', 2:'asdfghjkl', 3:'zxcvbnm'}
        result = []
        for word in words:
            rowid = -1
            valid = True
            if word[0].lower() in row[1]: rowid = 1
            if word[0].lower() in row[2]: rowid = 2
            if word[0].lower() in row[3]: rowid = 3
            for i in range(1,len(word)):
                if word[i].lower() not in row[rowid]:
                    valid = False
                    break
            if valid: result.append(word)
        return result
        
        
        
# Concise code

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rs = map(set, ['qwertyuiop','asdfghjkl','zxcvbnm'])
        ans = []
        for word in words:
            wset = set(word.lower())
            if any(wset <= rset for rset in rs):
                ans.append(word)
        return ans

        

