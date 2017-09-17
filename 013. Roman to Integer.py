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


    
import java.util.HashMap;


public class Roman {
	public static int romanToInteger(String s) throws Exception {
		if (s.length() == 0 || s == null) {
		        return 0;
		}
		HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
		dict.put('I', 1);
		dict.put('V', 5);
		dict.put('X', 10);
		dict.put('L', 50);
		dict.put('C', 100);
		dict.put('D', 500);
		dict.put('M', 1000);
		int len = s.length();
		int result = dict.get(s.charAt(len - 1));
		// check illegal input
		int sameCount = 1;
		for (int i = 0; i < len; i++) {
			if (!dict.containsKey(s.charAt(i))) {
				throw new Exception("Illegal input: invalid character " + s.charAt(i));
			}
			if (i < len - 1 && dict.get(s.charAt(i)) < dict.get(s.charAt(i + 1))) {
				int diff = dict.get(s.charAt(i + 1)) - dict.get(s.charAt(i));
				if (diff != 4 && diff != 9 && diff != 40 && diff != 90 && diff != 400 && diff != 900) {
					throw new Exception("Illegal input: invalid sequence " + s.charAt(i) + s.charAt(i + 1));
				}
			}
			if (i > 0 && s.charAt(i) == s.charAt(i - 1)) {
				sameCount++;
			} else {
				sameCount = 1;
			}
			if (sameCount > 1) {
				if (s.charAt(i) == 'V' || s.charAt(i) == 'L' || s.charAt(i) == 'D') {
					throw new Exception("Illegal input: 2 or more consecutive " + s.charAt(i));
				}
			}
			if (sameCount > 3) {
				throw new Exception("Illegal input: 4 or more consecutive " + s.charAt(i));
			}
		}
		
		for (int i = 0; i < len - 1; i++) {
		    if (dict.get(s.charAt(i)) >= dict.get(s.charAt(i + 1))) {
		        result += dict.get(s.charAt(i));
		    } else {
		        result -= dict.get(s.charAt(i));
		    }
		}
		return result;
	}
