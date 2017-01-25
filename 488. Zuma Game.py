'''
Problem:

Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). 
Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
'''


'''
Solution: dfs + cache

每一次尝试在board中插入若干个小球，达到消去小球的目的。

插入小球的原则如下：

1. 每一次插入小球（1个或者2个相同颜色球）至少引发一次“消除动作”，否则就不插入

2. 对于board中出现的连续相同颜色，只在最右侧进行插入
'''

class Solution(object):

    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        
        def removeMoreBalls(board):
            count = 1 
            removed = False
            for i in range(1,len(board)):
                if board[i] == board[i-1]:
                    count += 1
                else:
                    if count >= 3:
                        board = board[:i-count]+board[i:]
                        removed = True
                        break
                    count = 1
            if removed:
                removeMoreBalls(board)
                        
            return board
            
            
        def getMinStep(board, totalBalls, cache):    
            if not board: return 0
            if not totalBalls: return -1
            if board in cache: return cache[board]
            
            size = len(board)
            ans = -1
            nballs = 1
            for x in range(1, len(board) + 1):
                if x < len(board) and board[x] == board[x - 1]:
                    nballs += 1
                else:
                    if totalBalls[board[x - 1]] + nballs > 2:
                        ballneed = max(0, 3 - nballs)
                        totalBalls[board[x - 1]] -= ballneed
                        newBoard = removeMoreBalls(board[:x - nballs] + board[x:])
                        nans = getMinStep(newBoard, totalBalls, cache)
                        totalBalls[board[x - 1]] += ballneed
                        if nans != -1 and (ans == -1 or nans + ballneed < ans):
                            ans = nans + ballneed
                    nballs = 1
            cache[board] = ans
            return ans
    
    
        cache = {}
        totalBalls = collections.Counter(hand)
        return getMinStep(board, totalBalls, cache)
