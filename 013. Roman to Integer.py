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

    Let’s work through some examples. Assume the input is “VII”, using the [additive notation], we could simply add up each roman literal, ‘V’ + ‘I’ + ‘I’ = 5 + 1 + 1 = 7.
    
    Now let’s look at another example input “IV”. Now we need to use the [subtractive notation]. We first look at ‘I’, and we add 1 to it. 
    Then we look at ‘V’ and since a smaller roman literal ‘I’ appears before it, we need to subtract ‘I’ from ‘V’. 


    Time: O(n)
    Space: O(n) space
'''

class Solution:
    def romanToInt(self, s):

        roman_dic = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}
        strl = list(s)
        a = [roman_dic.get(v) for v in strl]
        res = list(a)
        for i,v in enumerate(a):
            if i < len(a)-1 and a[i]<a[i+1]:
                res[i]=-v
            else:
                res[i]=v
        return sum(res)
