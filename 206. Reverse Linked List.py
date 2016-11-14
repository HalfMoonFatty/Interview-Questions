'''
Problem:

Reverse a singly linked list.
A linked list can be reversed either iteratively or recursively.
Could you implement both?
'''


# Recursive

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case:
        if not head or not head.next:
            return head

        # divide the list
        first = head
        rest = first.next

        # reverse the rest of the linked list and remember the newhead
        newHead = self.reverseList(rest)

        # reverse the current node
        first.next.next = first
        first.next = None

        return newHead
        
        
        
# Iteratve:

class Solution:

    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = head
        r = None
        while p:
            q = p.next  
            p.next = r
            r = p
            p = q
        return r
