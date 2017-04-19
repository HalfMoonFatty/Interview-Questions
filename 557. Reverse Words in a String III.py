'''
Problem:

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''


# Solution 1:

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(w[::-1] for w in s.split())
        

# Solution 2: 不使用split与内置函数逆置的解法

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        charlist = list(s)
        
        start = end = i = j = 0
        
        while i < len(s):
        
            # find the last char of the word
            while i < len(s) and s[i] != ' ':
                i += 1
                
            # reverse the current word
            start, end = j, i-1
            while start < end:
                charlist[start],charlist[end] = charlist[end],charlist[start]
                start += 1
                end -= 1
                
            # move to next word
            i = j = i + 1
            
        return ''.join(charlist)


