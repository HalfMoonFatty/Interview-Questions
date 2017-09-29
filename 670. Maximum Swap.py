'''
Problem:

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 

Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Note: The given number is in the range [0, 108]
'''


# Time: O(n)
# Space: O(1)

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        lnum = list(str(num))
        last = {int(v): i for i, v in enumerate(lnum)}
        for i in range(len(lnum)):
            for digit in range(9, int(lnum[i]), -1):
                if last.get(digit, -1) > i:
                    lnum[i], lnum[last[digit]] = lnum[last[digit]], lnum[i]
                    return int("".join(lnum))
        return int(num)
    
    
    
    
'''
'''


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10: return num
        
        lnum = list(str(num))
        maxBehind = [None] * len(lnum)
        maxBehind[-1] = [lnum[-1], len(lnum)-1]
        for i in range(len(lnum)-2,-1,-1):
            if lnum[i] <= maxBehind[i+1][0]:
                maxBehind[i] = maxBehind[i+1]
            else:
                maxBehind[i] = [lnum[i], i]
        
        print maxBehind
        for i,n in enumerate(lnum):
            if maxBehind[i][0] > lnum[i]:
                lnum[i], lnum[maxBehind[i][1]] = lnum[maxBehind[i][1]], lnum[i]
                break
        
        return int(''.join(lnum))

            
            
