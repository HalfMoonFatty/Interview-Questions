'''
Problem:

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. 
The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 

Note: The value of n won't exceed 100,000.
'''



# TLE
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isValid(s):
            return s.count('A') <=1 and 'LLL' not in s
        
        def genRecord(i, n, record, count):
            if i == n and isValid(record):
                count[0] += 1
                return
            elif i < n:
                for s in ["A","L","P"]:
                    genRecord(i+1, n, record+s, count)
        
        count = [0]
        genRecord(0, n, '', count)
        return count[0]
            
