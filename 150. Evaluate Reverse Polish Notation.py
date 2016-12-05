'''
Problem:

    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Further Thoughts:
The above code contains duplication. For example, if we decide to add a new operator, we would need to update the code in two places – in the set’s initialization and the switch statement. Could you refactor the code so it is more extensible?

You are probably not expected to write this refactored code during an interview session. However, it will make you a stronger candidate if you could make this observation and point this out, as it shows to the interviewer that you care about clean code.

In Java, create an interface called Operator and map each operator string to an implementation of the Operator interface. For other languages such as C++, each operator will be mapped to a function pointer instead.

'''


class Solution(object):
    def evalRPN(self, tokens):
        """
            :type tokens: List[str]
            :rtype: int
            """
        def cal(num1,num2,operator):
            if operator == "+": return num1 + num2
            elif operator == "-": return num1 - num2
            elif operator == "*": return num1 * num2
            else: return int(num1/num2)


        operators = set(["+","-","*","/"])
        stack = []
        for token in tokens:
            if token in operators:
                num2 = float(stack.pop())
                num1 = float(stack.pop())
                stack.append(cal(num1,num2,token))
            else:
                stack.append(float(token))

        return int(stack[-1])
