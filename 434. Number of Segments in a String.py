'''
Problem:

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
'''

# Solution 1:
class Solution(object):
    def countSegments(self, s):
        return len(s.split())
        


# Solution 2:
# Time complexity:  O(n)
# Space complexity: O(1)

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segment = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                segment += 1
        return segment
