'''
Problem:

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

'''

def judgeCircle(self, moves):
    c = collections.Counter(moves)
    return c['L'] == c['R'] and c['U'] == c['D']
    
    
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        UDcount = LRcount = 0
        
        for m in moves:
            if m == "U":
                UDcount += 1
            elif m == "D":
                UDcount -= 1
            elif m == "L":
                LRcount += 1
            elif m == "R":
                LRcount -= 1
        return UDcount == LRcount == 0
