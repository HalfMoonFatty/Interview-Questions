'''
Problem:

Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. 
You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, 
T and F (T and F represent True and False respectively).

Note:
The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.


Example 1:
Input: "T?2:3"
Output: "2"
Explanation: If true, then result is 2; otherwise result is 3.


Example 2:
Input: "F?1:T?4:5"
Output: "4"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"


Example 3:
Input: "T?T?F:5:3"
Output: "F"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"
'''

'''
Solution:

循环直到栈中元素为1并且表达式为空：

取栈顶的5个元素，判断是否为一个可以解析的表达式。若是，则解析后压栈

否则 “从右向左” 将expression中的字符压入栈stack
'''

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        exprList = list(expression)
        while len(stack) > 1 or exprList:
            expr = stack[-5:]
            if len(expr) == 5 and expr[3] == '?' and expr[1] == ':':
                expr = expr[2] if expr[4] == 'T' else expr[0]
                stack = stack[:-5] + [expr]
            else:
                stack.append(exprList.pop())
        return stack[0] if stack else None
