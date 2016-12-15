'''
Problem:

Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
    str = "aabbcc", k = 3
    Result: "abcabc"
    The same letters are at least distance 3 from each other.


Example 2:
    str = "aaabc", k = 3
    Answer: ""
    It is not possible to rearrange the string.


Example 3:
    str = "aaadbbcc", k = 2
    Answer: "abacabcd"
    Another possible answer is: "abcabcda"
    The same letters are at least distance 2 from each other.
    
'''



'''
Solution:
                                 max heap
              ┏━━━━━━━━┓       ┏━━━━━━┓
     Str -->  ┃ Counter ▎  -->  ┃ heapq ▎ --> result
              ┗━━━━━━━━┛       ┗━━━━━━┛
                                  ↓   ↑  heapq.heappush(remaining, [front[0], front[1]])
        waitq.append([[0]+1,[1]]) ↓   ↑  if front[0] < 0
                                ┏━━━━━━┓
                                ┃ waitq ▎
                                ┗━━━━━━┛
                
'''


from collections import Counter, deque
import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        """
            :type str: str
            :type k: int
            :rtype: str
            """
            
        result = ""
        waitq = deque()
        
        remaining = []
        counter = Counter(str)
        for key,value in counter.items():
            heapq.heappush(remaining, [-1*value,key])
        

        while len(remaining) > 0:
            maxfre = heapq.heappop(remaining)
            result += maxfre[1]
            # note that char with 0 count still needs to be placed in waitQueue as a place holder
            waitq.append([maxfre[0]+1,maxfre[1]])

            if len(waitq) < k:
                continue

            # release from waitQueue if char is already k apart
            front = waitq.popleft()

            if front[0] < 0:
                heapq.heappush(remaining, [front[0], front[1]])

        return result if len(result) == len(str) else ""
