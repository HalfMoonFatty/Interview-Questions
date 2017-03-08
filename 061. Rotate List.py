'''
Problem:

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

class Solution(object):
    def rotateRight(self, head, k):

        if not head: return head
        
        # get the length of the list
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        # link the tail of the list with the head, make it a cycle
        tail.next = head

        # count down 1 less so head is prev of new head
        for i in range(length-k%length-1):
            head = head.next;

        # cut the linked list
        newHead = head.next;
        head.next = None;

        return newHead;
