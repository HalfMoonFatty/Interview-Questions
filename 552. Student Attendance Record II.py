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


'''
Soluion: DP

dp[i]the number of all possible attendance (without 'A') records with length i :

end with "P": dp[i-1]
end with "PL": dp[i-2]
end with "PLL": dp[i-3]
end with "LLL": is not allowed
so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

the number of all possible attendance (with 'A') records with length n:
∑dp[i] *dp[n-1-i] i = 0,1,...,n-1

Time Complexity O(n)
Space Complexity O(n)

(In code nums[i+1] means dp[i])
'''

class Solution(object):
    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result




# TLE
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        def genRecord(i, n, absent, record, count):
            if i == n:
                count[0] += 1
                return
            elif i < n:
                if not absent:
                    genRecord(i+1, n, True, record+"A", count)
                
                if len(record) < 2 or (len(record) >= 2 and not (record[-1] == "L" and record[-2] == "L")):
                    genRecord(i+1, n, absent, record+"L", count)

                genRecord(i+1, n, absent, record+"P", count)

        
        count = [0]
        genRecord(0, n, False, '', count)
        return count[0]
            

