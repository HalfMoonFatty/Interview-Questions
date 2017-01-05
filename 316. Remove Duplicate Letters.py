'''
Problem:

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

'''


# Time: O(n)
# Space: O(n)


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        charSet = set()   # charset represents chars currently in the stack
        stack = []
        
        for c in s:
            counter[c] -= 1
            
            if c in charSet:
                continue
                
            while stack and stack[-1] > c and counter[stack[-1]]:
                charSet.remove(stack.pop())
                
            charSet.add(c)
            stack.append(c)
            
        return ''.join(stack)
        
