'''
Problem:

    Implement a basic calculator to evaluate a simple expression string.
    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
    The integer division should truncate toward zero.
    You may assume that the given expression is always valid.

Some examples:
    "3+2*2" = 7
    " 3/2 " = 1
    " 3+5 / 2 " = 5

Note:
    Do not use the eval built-in library function.
'''




class Solution(object):
    def calculate(self, s):

        if not s: return 0
            
        stack = []
        sign = "+"
        number = ''

        # first loop calculate all "*" and "/" operations
        for i in range(len(s)):

            if s[i].isdigit():
                number += s[i]

            if (s[i] in ["+","-","*","/"]) or (i == len(s)-1):    # 看见operator说明刚刚的number已经结束了
                if sign == "+":
                    stack.append(int(number))
                elif sign == "-":
                    stack.append(-int(number))
                elif sign == "*":
                    stack.append(stack.pop()*int(number))
                else: # sign == '/'
                    stack.append(int(float(stack.pop())/float(number)))   # note float
                    
                sign = s[i]
                number = ''


        # second loop calculate the "+" and "-" operations ("-" operation is negative number)
        return sum(stack)
