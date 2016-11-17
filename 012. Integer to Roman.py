'''
Problem:

    Given an integer, convert it to a roman numeral.

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


    First, let’s understand how to read roman numerals. The rule of roman numerals is simple: Symbols are placed from left to right starting with the largest, and we add the values according to the additive notation. 
    However, there is an exception to avoid four symbols being repeated in succession, also known as the subtractive notation.


    The additive notation:
    We combine the symbols and add the values. For example, III is three ones, which is 3. Another example XV means ten followed by a five, which is 15.


    The subtractive notation:
    Four characters are avoided being repeated in succession (such as IIII). Instead, the symbol I could appear before V and X to signify 4 (IV) and 9 (IX) respectively. 
    Using the same pattern, we observe that X could appear before L and C to signify 40 (XL) and 90 (XC) respectively. The same pattern could be applied to C that is placed before D and M.


    With our understanding of roman numerals, we have to decide how to extract the digits from the integer. Should we extract from right to left (from the least significant digit) or from left to right (from the most significant digit)?
    If digits are extracted from right to left, we have to append the symbols in reversed order. Extracting digits from left to right seem more natural. It is also slightly trickier but not if we know the maximum number of digits could the number have in advanced, which we do – The number is within the range from 1 to 3999.

    Using the additive notation, we convert to roman numerals by breaking it so each chunk can be represented by the symbol entity. For example, 11 = 10 + 1 = “X” + “I”. Similarly, 6 = 5 + 1 = “V” + “I”. Let’s take a look of an example which uses the subtractive notation: 49 = 40 + 9 = “XL” + “IX”. Note that we treat “XL” and “IX” as one single entity to avoid dealing with these special cases to greatly simplify the code.


    所以最重要的是，将4和9，40，90，400，900include 进来，以减少subtractive notation。
    以下就是修改版的 Roman to int 的 mapping:
    roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

'''

class Solution(object):
    def intToRoman(self, num):
        """
            :type num: int
            :rtype: str
            """
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        res = ''
        for i in range(13):
            if num >= val[i]:
                count = num/val[i]
                num%=val[i]
                for j in range(count):      # note here "j"
                    res += roman[i]         # here "i"

        return res
