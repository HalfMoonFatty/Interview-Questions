'''
Problem:

    You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to 
    remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

    Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game 
    given the number of stones in the heap.

    For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, 
    the last stone will always be removed by your friend.

Hint:
    If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?

'''

class Solution(object):
    def canWinNim(self, n):

        return n % 4 != 0
        # return ((n - 1) % 4 == 0 or  (n - 2) % 4 == 0 or (n - 3) % 4 == 0)
        # as you are the first one, you can pick 1, 2, or 3 then check if the left is n*4 and it is the other's turn...
