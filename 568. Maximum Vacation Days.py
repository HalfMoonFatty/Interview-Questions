'''
Problem:

LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. 
But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the 
traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

Rules and restrictions:

- You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.

- The flights are represented as a N*N matrix (not necessary symmetrical), called flights representing the airline status from city i to city j. 
  If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.

- You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each 
  week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.

- For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. 
  For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.


You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.

Example 1:

Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation: Ans = 6 + 3 + 3 = 12. 

One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
(Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.


Example 2:

Input:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
Output: 3
Explanation: Ans = 1 + 1 + 1 = 3. 

Since there is no flights enable you to move to another city, you have to stay at city 0 for the whole 3 weeks. 
For each week, you only have one day to play and six days to work. 
So the maximum number of vacation days is 3.


Example 3:

Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
Output: 21
Explanation: Ans = 7 + 7 + 7 = 21

One of the best strategies is:
1st week : stay at city 0, and play 7 days. 
2nd week : fly from city 0 to city 1 on Monday, and play 7 days.
3rd week : fly from city 1 to city 2 on Monday, and play 7 days.


Note:
N and K are positive integers, which are in the range of [1, 100].
In the matrix days, all the values are integers in the range of [0, 1].
In the matrix flights, all the values are integers in the range [0, 7].
You could stay at a city beyond the number of vacation days, but you should work on the extra days, which won't be counted as vacation days.
If you fly from the city A to the city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
We don't consider the impact of flight hours towards the calculation of vacation days.
'''


'''
Solution 1: DP

dp[w][c]表示第w周选择留在第c个城市可以获得的最大总收益

初始令dp[0][0] = days[0][0], dp[w][1 .. c - 1] = days[c][0] if flights[0][c]

当dp[w][c] < 0时，表示第c个城市在第w周时还不可达。

状态转移方程：

for w in (0 .. K)
    for sc in (0 .. N)
        if dp[w][sc] < 0:
            continue
        for tc in (0 .. N)
            if sc == tc or flights[sc][tc] == 1:
                dp[w + 1][tc] = max(dp[w + 1][tc], dp[w][sc] + days[tc][w])


Time: O(N^2)
Space: O(N^2)
'''

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N, K = len(days), len(days[0])
        dp = [[-1] * N for _ in range(K)]

        dp[0][0] = days[0][0]
        for c in range(1,N):
            if flights[0][c]:
                dp[0][c] = days[c][0] 

        for w in range(1,K):
            for sc in range(N):
                if dp[w-1][sc] < 0: continue
                for tc in range(N):
                    if sc == tc or flights[sc][tc]:
                        dp[w][tc] = max(dp[w][tc], dp[w-1][sc] + days[tc][w])
        return max(dp[-1])
        
        
        
        
# Optimization: Time: O(N^2); Space O(N)

class Solution(object):

    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        dp = [0] + [-1] * (N - 1)
        for w in range(K):
            ndp = [x for x in dp]
            for sc in range(N):
                if dp[sc] < 0: continue
                for tc in range(N):
                    if sc == tc or flights[sc][tc]:
                        ndp[tc] = max(ndp[tc], dp[sc] + days[tc][w])
            dp = ndp
        return max(dp)
        
