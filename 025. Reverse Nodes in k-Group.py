'''
Problem:

    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    You may not alter the values in the nodes, only nodes itself may be changed.
    Only constant memory is allowed.

For example,
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5


'''


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 2: return head
        
        n = 0
        dummy = ListNode(-1)
        dummy.next = head
        cur, nxt, pre = dummy,dummy,dummy
        while cur.next:
            cur = cur.next
            n += 1
            
        while n >= k:
            cur = pre.next
            nxt = cur.next
            for i in range(k-1):
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = cur.next
            pre = cur
            n -= k
        return dummy.next
                
            


'''
Solution:
    Before review this problem "Swap Nodes in Pairs";
    After review this problem, check next problem: Sort List

    - Standard helper function: recusively reverse a linked list
    - in the reverseKGroup function, use dummy node: 1. esay to set up prev; 2. easy for return head

init
     dummy -> head -> ......-> None
       |
  prev,curtail

Step 1: Get all pointers ready, curhead and curtail are the head and tail pointers for the reverse part
    prev -|-> curhead -> ......-> curtail -|-> nxt ->

Step 2: Cut out the curtail to feed in the recusive reverse function
    prev -|-> curhead -> ......-> curtail --> None | nxt ->

Step 3: Reverse
    reverseLL(curhead)

Step 4: Relink the reversed part back to the linked list
    prev -|-> curtail -> ......-> curhead -|-> nxt ->

Step 5: Reset prev and curtail as in the init state outside the while loop
    .... -|-> curtail -> ......-> curhead -|-> nxt ->
                                     |
                                prev,curtail
                                
'''

class Solution(object):
    def reverseKGroup(self, head, k):
        """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            """

        def reverseLL(curhead):
            if not curhead:
                return
            first = curhead
            rest = first.next
            if not rest:
                return
            reverseLL(rest)
            first.next.next = first
            first.next = None
            return

        # sanity check
        if not head or k < 2:
            return head

        # init state
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curtail = prev

        while True:
            count = 0
            while count < k and curtail:
                curtail = curtail.next
                count += 1

            # not enough k nodes to the tail, so no need further reverse
            if not curtail:
                break

            # Step 1
            curhead = prev.next
            nxt = curtail.next
            # Step 2
            curtail.next = None
            # Step 3
            reverseLL(curhead)
            # Step 4
            prev.next = curtail
            curhead.next = nxt
            # Step 5
            prev = curtail = curhead

        return dummy.next
