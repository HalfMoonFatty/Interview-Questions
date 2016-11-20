'''
Problem:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


# Time: O(n)
# Space: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def match(front, back):
            return (front == '(' and back == ')') or (front == '[' and back == ']') or (front == '{' and back == '}')


        if not s: return True
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0 or not match(stack.pop(),char): 
                    return False

        return len(stack) == 0     # note      
