'''
Problem:
   
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
   
Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
   
Example:
   
// Init a singly linked list [1,2,3].
// getRandom() should return either 1, 2, or 3 randomly.
// Each element should have equal probability of returning.
// solution.getRandom();

'''

'''
Solution:

Choose k entries from n numbers. Make sure each number is selected with the probability of k/n


BASIC IDEA:

Choose 1, 2, 3, ..., k first and put them into the reservoir.
For k+1, pick it with a probability of k/(k+1), and randomly replace a number in the reservoir.
For k+i, pick it with a probability of k/(k+i), and randomly replace a number in the reservoir.
Repeat until k+i reaches n


PROOF:

For k+i, the probability that it is selected and will replace a number in the reservoir is k/(k+i)
For a number in the reservoir before (let's say X), the probability that it keeps staying in the reservoir is
P(X was in the reservoir last time) * P(X is not replaced by k+i)
= P(X was in the reservoir last time) * (1- P(X is replaced this time))
= k/(k+i-1) * (1 - k/(k+i) * 1/k) = k/(k+i)
When k+i reaches n, the probability of each number staying in the reservoir is k/n

'''


class Solution(object):
   
    def __init__(self, head):

        self.head = head
   
    def getRandom(self):

        def getRandK(k):
            cur = self.head
            res = [0]*k
            i = 0
           
            # init res with first k vals
            while cur and i < k:
                res[i] = cur.val
                cur = cur.next
                i += 1
           
            while cur:
                j = random.randint(0,i)
                if j < k:
                    res[j] = cur.val
                cur = cur.next
                i += 1
           
            return res
       
        return getRandK(1)[0]
