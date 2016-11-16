'''
Problem:

    You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -,
    you and your friend take turns to flip two consecutive "++" into "--". 
    The game ends when a person can no longer make a move and therefore the other person will be the winner.

    Write a function to determine if the starting player can guarantee a win.

    For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
     Derive your algorithm's runtime complexity.

'''

'''
Solution: Backtracking

We can basically try every possible move for the first player (Let's call him 1P from now on), 
and recursively check if the second player 2P has any chance to win. If 2P is guaranteed to lose, 
then we know the current move 1P takes must be the winning move.

Now let's check the time complexity: Suppose originally the board of size N contains only '+' signs, then roughly we have:

T(N) = T(N-2) + T(N-3) + [T(2) + T(N-4)] + [T(3) + T(N-5)] + ...
[T(N-5) + T(3)] + [T(N-4) + T(2)] + T(N-3) + T(N-2)
= 2 * sum(T[i])  (i = 3..N-2)
You will find that T(N) = 2^(N-1) satisfies the above equation. Therefore, this algorithm is at least exponential.

'''

class Solution(object):
    def canWin(self, s):
        """
            :type s: str
            :rtype: bool
            """
        def win(s):
            for i in range(len(s)-2+1):
                if s[i] == "+" and s[i+1] == "+":
                    s[i],s[i+1] = "-","-"
                    ans = not win(s)
                    s[i],s[i+1] = "+","+"
                    if ans:
                        return True
            return False

        return win(list(s))
