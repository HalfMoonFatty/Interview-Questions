'''
Problem:

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. 
The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers?
e.g. two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example
Input:   maxChoosableInteger = 10    desiredTotal = 11
Output:  false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
'''

'''
Solution:

The key part for the top-down memorization strategy is that we need to avoid repeatedly solving sub-problems. 
By applying the memorization, we at most compute for every subproblem once, and there are O(2^n) subproblems, 
so the complexity is O(2^n) after memorization. (Without memo, time complexity should be like O(n!))

For this question, the key part is: what is the state of the game? - The chosen/unchosen numbers

Use a boolean array(used) to denote which numbers have been chosen.
Since in the problem statement, it says maxChoosableInteger will not be larger than 20.
Then we can use an Integer(state) to represent this boolean[] array.

The rest part of the solution is just simulating the game process using the top-down dp.
'''


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):

        def convertToState(used):
            state = 0
            for bit in used:
                state <<= 1
                if bit: state |= 1
            return state
                    
            
        def canWin(desiredTotal, used, cache):
            if desiredTotal <= 0: 
                return False
            state = convertToState(used)
            if state not in cache:
                for i in range(1, len(used)):
                    if not used[i]:
                        used[i] = True
                        if not canWin(desiredTotal-i, used, cache):
                            cache[state] = True
                            used[i] = False
                            return True
                        used[i] = False
                cache[state] = False

            return cache[state]
            
                        
        if maxChoosableInteger >= desiredTotal: return True
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal: return False
        
        cache = {}
        used = [False] * (maxChoosableInteger+1)
        return canWin(desiredTotal, used, cache)
        
