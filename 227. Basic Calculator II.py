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
        prevSign = "+"
        prevNum = 0

        # first loop calculate all "*" and "/" operations
        for i in range(len(s)):

            if s[i].isdigit():
                prevNum = prevNum*10+int(s[i])
                
            if (s[i] in ["+","-","*","/"]) or (i == len(s)-1):
                if prevSign == "+":
                    stack.append(prevNum)
                elif prevSign == "-":
                    stack.append(-prevNum)
                elif prevSign == "*":
                    stack.append(stack.pop()*prevNum)
                else: # prevSign == '/'
                    stack.append(int(float(stack.pop())/float(prevNum)))
                    
                prevSign = s[i]
                prevNum = 0


        # second loop calculate the "+" and "-" operations ("-" operation is negative number)
        return sum(stack)
