'''
Problem:

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.


Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.


Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. 
And the output should be also in this form.
'''


'''
Solution:

e.g. "1+1i", "1+1i"

a = [u'1', u'1i'] 
b = [u'1', u'1i']

int(a[0]), int(b[0]) = 1, 1
a[1], b[1] = 1i, 1i
int(a[1][:1]), int(b[1][:-1]) = 1, 1
'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split("+")
        b = b.split("+")
        first = int(a[0]) * int(b[0]) - int(a[1][:-1]) * int(b[1][:-1])
        second = int(a[0]) * int(b[1][:-1]) + int(b[0]) * int(a[1][:-1])
        return str(first) + "+" + str(second) + "i"
