'''
Problem:

    Given a roman numeral, convert it to an integer.

    Input is guaranteed to be within the range from 1 to 3999.
'''

'''
Solution:

    本题的关键就是写下 Roman literals and its decimal representations 的 mapping array:

    Roman Literal   Decimal
    I               1
    V               5
    X               10
    L               50
    C               100
    D               500
    M               1000

    Let’s work through some examples. Assume the input is “VII”, using the [additive notation], we could simply add up each roman literal, 
    ‘V’ + ‘I’ + ‘I’ = 5 + 1 + 1 = 7.
    
    Now let’s look at another example input “IV”. Now we need to use the [subtractive notation]. We first look at ‘I’, and we add 1 to it. 
    Then we look at ‘V’ and since a smaller roman literal ‘I’ appears before it, we need to subtract ‘I’ from ‘V’. 


    Time: O(n)
    Space: O(n) space
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}
        vals = [roman_dic.get(v) for v in s]
        res = vals[:]
        for i in range(len(vals)):
            if i < len(vals)-1 and vals[i] < vals[i+1]:
                res[i] = -vals[i]
            else:
                res[i] = vals[i]
        return sum(res)
    
    
    
# Optimization
# Time: O(n)
# Space: O(1)
class Solution(object):
    def romanToInt(self, s):

        roman_dic = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}
        prev = 0
        total = 0

        for c in s:
            curr = roman_dic[c]
            total += (curr - 2 * prev) if prev < curr else curr
            prev = curr
        return total

