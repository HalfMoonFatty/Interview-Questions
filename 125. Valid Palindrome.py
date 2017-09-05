'''
Problem:

	Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

	For example,
	"A man, a plan, a canal: Panama" is a palindrome.
	"race a car" is not a palindrome.

Note:
	Have you consider that the string might be empty? This is a good question to ask during an interview.
	For the purpose of this problem, we define empty string as valid palindrome.

'''

class Solution(object):
    def isPalindrome(self, s):

        s =''.join(ch for ch in s if ch.isalnum())
        if not (s.strip()) or len(s) ==1:
            return True

        start,end = 0, len(s)-1
        while start<=end:
            if s[start].upper() == s[end].upper():
                start += 1
                end -= 1
            else:
                return False
        return True

# in-place

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #s =''.join(ch for ch in s if ch.isalnum())
        if not (s.strip()) or len(s) ==1:
            return True

        start,end = 0, len(s)-1
        while start <= end:
            while start <= end and not s[start].isalnum():
                start += 1
            while start <= end and not s[end].isalnum():
                end -= 1

            if start <= end:
                if s[start].upper() == s[end].upper():
                    start += 1
                    end -= 1
                else:
                    return False
        return True
