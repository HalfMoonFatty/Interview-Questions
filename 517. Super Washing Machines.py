'''
Problem:

You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine 
to one of its adjacent washing machines at the same time .

Given an integer array representing the number of dresses in each washing machine from left to right on the line, 
you should find the minimum number of moves to make all the washing machines have the same number of dresses. 
If it is not possible to do it, return -1.

Example1
Input: [1,0,5]
Output: 3
Explanation: 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   

Example2
Input: [0,3,0]
Output: 2
Explanation: 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     

Example3
Input: [0,2,0]
Output: -1
Explanation: 
It's impossible to make all the three washing machines have the same number of dresses. 

Note:
The range of n is [1, 10000].
The range of dresses number in a super washing machine is [0, 1e5].
'''


'''
Solution:

Since we can operate several machines at the same time, the minium number of moves is the maximum number of necessary operations on every machine.

For a single machine, necessary operations is to transfer dresses from one side to another until sum of both sides and itself reaches the average number. 
We can calculate (required dresses) - (contained dresses) of each side as L and R:

L > 0 and R > 0: both sides lacks dresses, and we can only export one dress from current machines at a time, so result is abs(L) + abs(R)
L < 0 and R < 0: both sides contains too many dresses, and we can import dresses from both sides at the same time, so result is max(abs(L), abs(R))
L < 0 and R > 0 or L >0 and R < 0: the side with a larger absolute value will import/export its extra dresses from/to current machine or other side, so result is max(abs(L), abs(R))

For example, [1, 0, 5], average is 2
for 1, L = 0 - 0 * 2 = 0, R = 2 * 2 - 5 = -1, result = 1
for 0, L = 1 * 2 - 1 = 1, R = 1 * 2 - 5 = -3, result = 3
for 5, L = 2 * 2 - 1 = 3, R = 0 * 2 - 0 = 0,  result = 3
so minium moves is 3
'''


class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        size = len(machines)
        if total % size: return -1
        
        avg = total / size
        sums = [0] * (size+1)
        for i in range(len(machines)):
            sums[i+1] += sums[i] + machines[i]

        ans = 0
        for i in range(size):
            left = i * avg - sums[i]
            right = (size - 1 - i) * avg - (sums[-1] - sums[i] - machines[i])
            if left > 0 and right > 0:
                ans = max(ans, left + right)
            else:
                ans = max(ans, abs(left), abs(right))
        return ans

    
# Solution 2: https://discuss.leetcode.com/topic/79938/super-short-easy-java-o-n-solution/7
