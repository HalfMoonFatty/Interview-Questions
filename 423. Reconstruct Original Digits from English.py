'''
Problem:


Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.

Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"

'''




class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0]*10
        for c in s:
            if c == 'z': count[0] += 1
            if c == 'w': count[2] += 1
            if c == 'x': count[6] += 1
            if c == 's': count[7] += 1 # 7-6
            if c == 'g': count[8] += 1
            if c == 'u': count[4] += 1
            if c == 'f': count[5] += 1 # 5-4
            if c == 'h': count[3] += 1 # 3-8
            if c == 'i': count[9] += 1 # 9-8-5-6
            if c == 'o': count[1] += 1 # 1-0-2-4
            
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]
        
        res = ''
        for i in range(10):
            for j in range(count[i]):
                res += str(i)
        return res
