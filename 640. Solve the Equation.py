'''
Problem:

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, 
the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"


Example 2:
Input: "x=x"
Output: "Infinite solutions"


Example 3:
Input: "2x=x"
Output: "x=0"


Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"


Example 5:
Input: "x=x+2"
Output: "No solution"
'''

'''
Solution:

用'='将等式分为左右两半

分别求左右两侧x的系数和常数值，记为 lcoeff, lconst, rcoeff, rconst

令 coefficient, constant = lcoeff - rcoeff, rconst - lconst

若x != 0，则x = c / x

否则，若c != 0，说明方程无解

否则，说明有无数组解
'''

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parseExpre(exp):
            val = ''
            coefficient = 0
            constant = 0
            sign = 1
            for e in exp + '#':
                if e in '+-#':
                    if val: constant += int(val)*sign 
                    sign = 1 if e == "+" else -1
                    val = ''
                elif e == "x":
                    if val: coefficient += int(val)*sign
                    else: coefficient += 1*sign
                    sign = 1 if e == "+" else -1
                    val = ''
                else:
                    val += e
            return [coefficient, constant]
                    
        left, right = equation.split("=")
        lcoeff, lconst = parseExpre(left)
        rcoeff, rconst = parseExpre(right) 
        coefficient, constant = lcoeff - rcoeff, rconst - lconst
        if coefficient == 0 and constant == 0: return "Infinite solutions"
        elif coefficient == 0: return "No solution"
        else: return 'x='+str(constant / coefficient)
        
        
        
        
