'''
Problem:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


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
                if len(stack) > 0 and match(stack.pop(),char): 
                    continue
                else:
                    return False

        return len(stack) == 0  
        
