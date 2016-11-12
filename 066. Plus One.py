'''
Problem:

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''


# Time: O(n)
# Space: O(1)


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            carry = digits[i]/10
            digits[i] %= 10

        return [1] + digits if carry == 1 else digits
