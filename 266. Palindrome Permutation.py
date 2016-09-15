'''
Problem:

    Given a string, determine if a permutation of the string could form a palindrome.

For example,
    "code" -> False, "aab" -> True, "carerac" -> True.

Hint:
    - Consider the palindromes of odd vs even length. What difference do you notice?
    - Count the frequency of each character.
    - If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
'''



class Solution(object):
    def canPermutePalindrome(self, s):
        """
            :type s: str
            :rtype: bool
            """
        st = set()
        for c in s:
            if c in st:
                st.remove(c)
            else:
                st.add(c)
        return (len(s)%2 == 0 and len(st) == 0) or (len(s)%2 == 1 and len(st) == 1)
