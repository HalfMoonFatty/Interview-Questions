'''
Problem:

Your task is to calculate a^b mod 1337 where a is a positive integer 
and b is an extremely large positive integer given in the form of an array.

    Example1:
    a = 2
    b = [3]
    Result: 8

    Example2:
    a = 2
    b = [1,0]
    Result: 1024

Similar Problem:
    (M) 50. Pow(x, n)

'''

'''
Solution 1: Recursive

ab % k = (a%k)(b%k)%k

e.g. a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k

'''

class Solution(object):
    def superPow(self, a, b):

        # base case
        if not b:
            return 1
        else:
            last_digit = b.pop()
            return pow(self.superPow(a, b),10,1337) * pow(a,last_digit,1337) % 1337
