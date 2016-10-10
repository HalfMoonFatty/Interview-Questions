'''
Problem:

Given a linked list, swap every two adjacent nodes and return its head.

For example, Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.

'''


'''
Solution:

    Swap pair nodes, remember to link the previous swapped node.next to the new swapped node.
    Linked list super trick is still using a DUMMY node.
'''

class Solution(object):
    def swapPairs(self, head):

        if not head or not head.next:
            return head
       
        cur = head
        next = cur.next
        prev = ListNode(-1)  # dummy node
        prev.next = head
        newhead = cur.next
       
        while cur and next:
            cur.next = next.next
            next.next = cur
            prev.next = next   # note
            prev = cur
            cur = cur.next
            if not cur:
                break
            next = cur.next
       
        return newhead

