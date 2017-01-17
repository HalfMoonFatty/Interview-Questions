'''
Problem:
    Given an integer n, return 1 - n in lexicographical order.
    For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
    Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''

class Solution(object):
    def lexicalOrder(self, n):

        def dfs(res,result):
            if res <= n:
                result.append(res)
            if res*10 <= n:    # optimization
                for i in range(10):
                    dfs(res*10+i, result)


        result = []
        for i in range(1,10):    # first bit cannot be 0
            dfs(i,result)
        return result
   
   
   
'''
Problem:

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
Note: 1 ≤ k ≤ n ≤ 109.

Example:
Input: n: 13   k: 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
'''

'''
Solution:
Initially, image you are at node 1 (variable: curr),
the goal is move (k - 1) steps to the target node x. (substract steps from k after moving)
when k is down to 0, curr will be finally at node x, there you get the result.
                                  0
            /                 /         |  \   \
           1                 2      ... 7   8   9
      /  |  \ ... \       / / | \
     10 11 12 ... 19    20 21 22 23...
    / | \              / | \
100 101 102 103...   200 201 202 203...

Main function
    Firstly, calculate how many steps curr need to move to curr + 1.
    if the steps <= k, we know we can move to curr + 1, and narrow down k to k - steps.
    else if the steps > k, that means the curr + 1 is actually behind the target node x in the preorder path, we can't jump to curr + 1. 
    What we have to do is to move forward only 1 step (curr * 10 is always next preorder node) and repeat the iteration.

calSteps function - to calculate by level.
    Let n1 = curr, n2 = curr + 1.
    n2 is always the next right node beside n1's right most node (2 is right next to 1, 20 is right next to 19, 200 is right next to 199).
    so, if n2 <= n, what means n1's right most node exists, we can simply add the number of nodes from n1 to n2 to steps.
    else if n2 > n, what means n (the biggest node) is on the path between n1 to n2, add (n + 1 - n1) to steps.
    organize this flow to "steps += Math.min(n + 1, n2) - n1; n1 *= 10; n2 *= 10;"
    e.g. 
    n1 = 1, n2 = 2, step = n2-n1 = 1    (1 step between 1 and 2)
    n1*10 = 10, n2*10 = 20, step = n2-n1 = 10    (10 step between 10 and 20)
    n1*10 = 100, n2*10 = 200, step = n2-n1 = 100    (100 step between 100 and 200)
    ... increase the step *10 every time, until n1 > n
'''


class Solution(object):
    def findKthNumber(self, n, k):

        def calSteps(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n+1, n2) - n1
                n1 *= 10
                n2 *= 10
            return step
        
        
        curr = 1
        k -= 1
        while k > 0:
            step = calSteps(n, curr, curr+1)
            if step <= k :
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr
            
