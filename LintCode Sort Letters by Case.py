'''
Problem:

	Given a string which contains only letters. Sort it by lower case first and upper case second.

Note:
	It's NOT necessary to keep the original order of lower-case letters and upper case letters.

'''

'''
Solution 2 pointers
'''
import string
class Solution:
    def sortLetters(self, chars):
        i,j = 0, len(chars)-1
        while i <= j:
            while i <= j and chars[i] in string.lowercase:
                i += 1
            while i <= j and chars[j] in string.uppercase:
                j -= 1
            if i <= j:
                chars[i],chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return
