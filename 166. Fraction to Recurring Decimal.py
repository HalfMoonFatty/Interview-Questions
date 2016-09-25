'''
Problem:

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
     If the fractional part is repeating, enclose the repeating part in parentheses.

For example,
Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

Hint:
No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

'''


# Solution: quo -> decimal point -> reminder recurrence -> reminder

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
            :type numerator: int
            :type denominator: int
            :rtype: str
            """

        res = ''
        if denominator == 0 or numerator == 0: return '0'
        
        negativeFlag = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        dec = False
        recurMap = {}

        while True:
            quo = numerator/denominator
            rem = numerator%denominator
            res += str(quo)

            if int(rem) == 0: # (1) no fractional part; (2) fractional part does not recur;
                break

            if not dec: # first decimal
                res += '.'
                dec = True

            if recurMap.has_key(rem): # recurrence happened, find the index to insert "()"
                ind = recurMap[rem]
                res = res[:ind] + "(" + res[ind:] + ")"
                break
            else:
                recurMap[rem] = len(res)

            if rem < denominator:
                numerator = rem*10
        
        
        return res if not negativeFlag else '-' + res
        
