'''
Problem:

     Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
    Could negative integers be palindromes? (ie, -1)
    If you are thinking of converting the integer to string, note the restriction of using extra space.
    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
    There is a more generic way of solving this problem.
'''



# Solution 1: Only compare half of the digits in x, so don't need to deal with overflow.
 

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x%10 == 0): return False
        rev = 0
        while x > rev:
            rev = rev*10 + x%10
            x /= 10
        return x == rev or x == rev/10




# Solution 2: 2 pointers


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = 1
        while x/y >= 10:
            y *= 10
       
        while x:
            if x/y != x%10:
                return False
            x = (x%y)/10
            y /= 100
        return True





