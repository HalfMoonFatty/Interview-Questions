'''
Problem:
   
    Validate if a given string is numeric.
   
    Some examples:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
   
Note:
    It is intended for the problem statement to be ambiguous.
    You should gather all requirements up front before implementing one.
   
Similar Problems:
    (E) String to Integer (atoi)
   
'''

'''
Solution:
    题不难就是corner cases 特别多， 繁琐。
   
    - Remove all white chars
    - Sign : signs occur in the middle: must be "e+?" pattern so +/- cannot be the last one in this string...
    - Exp : e,E has already occured; or digit never occured;  "E" 的前面不能有sign; or e/E is the last
    - Decimal : decimal already occured; e/E already occured; "." 的前面不能有"E"; decimal is the lastone but digit never occured; like -., e., E.....
    - Digit : used for other "exp","decimal" checks Turn digit to True if met...
'''

class Solution:
   
    def isNumber(self, s):
        s = s.strip() #remove white chars
       
        digit = False
        decimal = False
        exp = False
        sign = False
       
       
        if not s or (len(s)==1 and not "0"<=s<="9"):
            return False
       
        for i in range(len(s)):
           
            if i == 0:
                if s[i] == '+' or s[i] == '-':
                    sign = True
                elif s[i] == '.':
                    decimal = True
                elif '0'<=s[i]<= '9':
                    digit = True
                else:
                    return False
       
            elif s[i] == "+" or s[i] == "-":
                if (s[i-1] == 'e' or s[i-1] == 'E') and i<len(s)-1 and '0'<=s[i+1]<='9':
                    continue
                else:
                    return False

            elif s[i] == "e" or s[i] == "E":
                if exp or (not digit) or s[i-1] == "+" or s[i-1] == "-" or i == len(s)-1:
                    return False
                else:
                    exp = True
                    continue

            elif s[i] == ".":
                if decimal or exp or s[i-1] == 'e' or s[i-1] == 'E' or (i == len(s)-1 and not digit):
                    return False
                else:
                    decimal = True
                    continue

            elif "0" <= s[i] <= "9":
                digit = True
                continue

            else:
                return False


        return True
