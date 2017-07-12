'''
Problem:

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"

Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:
Input:"1/3-1/2"
Output: "-1/6"

Example 4:
Input:"5/3+1/3"
Output: "2/1"

Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

'''


'''
Solution:

新分母 = 原分母的最小公倍数，即(denom = LCM)

新分子 = sum(将原分子乘以 LCM / 原分母)

求 "新分母" 和 "新分子" 的最大公约数的绝对值，记为GCD

结果的分子分母分别为HI / GCD, LO / GCD
'''



class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # 最大公约数
        def gcd(a,b):
            if a < b: a,b = b,a
            while b:
                a,b = b, a%b
            return a
        
        # 最小公倍数
        def lcm(a,b):
            return a*b/gcd(a,b)
        
        
        # parce expression
        part = ''
        fractions = []
        for c in expression:
            if c in ['+','-']:
                if part: fractions.append(part)
                part = ''
            part += c
        fractions.append(part)
        
        numerator = [int(e.split('/')[0]) for e in fractions]
        denominator = [int(e.split('/')[1]) for e in fractions]
        
        
        # calculation
        denom = denominator[0]
        numer = numerator[0]
        for i in range(1,len(denominator)):
            denom = lcm(denom,denominator[i])  # denom = LCM
        numer = sum(n * denom / d for n, d in zip(numerator, denominator))
        GCD = abs(gcd(denom, numer))

        return str(numer / GCD) + "/" + str(denom / GCD)
