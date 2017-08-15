'''
Problem:

Imagine you have a special keyboard with the following keys:

Key 1: (A): Prints one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A


Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V


Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.

'''

'''
Solution:

We use i steps to reach maxA(i) then use the remaining n - i steps to reach n - i - 1 copies of maxA(i)

For example:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Here we have n = 7 and we used i = 3 steps to reach AAA
Then we use the remaining n - i = 4 steps: Ctrl A, Ctrl C, Ctrl V, Ctrl V, to reach n - i - 1 = 3 copies of AAA

We either don't make copies at all, in which case the answer is just n, or if we want to make copies, 
we need to have 3 steps reserved for Ctrl A, Ctrl C, Ctrl V so i can be at most n - 3
'''

class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [i for i in range(N+1)]
        for i in range(N+1):
            for j in range(1, i-2):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[-1]
