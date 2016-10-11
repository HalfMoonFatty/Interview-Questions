'''
Problem:

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
     Given 1->4->3->2->5->2 and x = 3,
     return 1->2->2->4->3->5.
'''


'''
Solution:

Time: O(n)
Space: O(n)

'''


class Solution(object):
    def partition(self, head, x):

        if not head: return None

        ltcur = ltlist = ListNode(0)    # dummy node for val < x
        gtcur = gtlist = ListNode(0)    # dummy node for val >= x

        # iterate the ll and partion into 2 lists
        while head:
            if head.val < x:
                ltcur.next = head
                ltcur = ltcur.next
            else:
                gtcur.next = head
                gtcur = gtcur.next
            head = head.next

        lthead = ltlist.next
        gthead = gtlist.next

        # concatenate 2 lists, need to check if the list heads are None
        if ltcur: ltcur.next = gthead
        if gtcur: gtcur.next = None
        return lthead if lthead else gthead

        
