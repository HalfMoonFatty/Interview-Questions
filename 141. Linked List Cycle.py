'''
Problem:

    Given a linked list, determine if it has a cycle in it.

Follow up:
    Can you solve it without using extra space?

'''

'''
Solution 1: Fast Slow pointers

'''

class Solution(object):

    def hasCycle(self, head):

        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
