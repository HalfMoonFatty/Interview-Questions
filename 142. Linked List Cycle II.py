Problem:

	Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note:
    Do not modify the linked list.

Follow up:
    Can you solve it without using extra space?

'''

class Solution(object):

    def detectCycle(self, head):

        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        # out of the loop becasue of fast.next is None
        # i.e. no loop
        if not fast or not fast.next:
            return None

        # Move meetPoint to Head. Keep fast at Meeting Point.
        # Each are k steps from the Loop Start.
        # If they move at the same pace, they must meet at Loop Start.
        meetPoint = head
        while meetPoint != fast:
            meetPoint = meetPoint.next
            fast = fast.next
        return meetPoint
