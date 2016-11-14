'''
Problem:

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

'''

'''
Solution:

Time: O(N)
Space: O(1)
'''

class Solution(object):
    def removeElements(self, head, val):
        """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        cur = head
        while cur:
            if cur.val == val
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
        
