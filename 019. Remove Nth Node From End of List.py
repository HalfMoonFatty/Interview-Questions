'''
Problem:

    Given a linked list, remove the nth node from the end of list and return its head.

    For example,
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
    Given n will always be valid.
    Try to do this in one pass.
'''

class Solution(object):

    def removeNthFromEnd(self, head, n):

        if not head:
            return None

        # make dummy head
        dummy = ListNode(0)
        dummy.next = head

        # both fast and slow from dummy head
        fast, slow = dummy, dummy

        # move the fast pointer n steps ahead
        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
