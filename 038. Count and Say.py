'''
Problem:

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


'''
Solution:

Time:O(n)
Space:O(n)
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = "1"            # init last string
        for i in range(n-1):
            prev = s[0]    # previous character
            count = 1      # count of repeated chars
            ss = ''        # new string built
            for j in range(1,len(s)):
                if s[j] == prev:    # meet an old char
                    count += 1
                else:               # meet a new char
                    ns += str(count) + prev    
                    prev = s[j]                   
                    count = 1                  
            ns += str(count) + prev       # append the last substring from the loop
            s = ns
        return s
