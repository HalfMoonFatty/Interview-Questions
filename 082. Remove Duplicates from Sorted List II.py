'''
Problem:

Given a sorted linked list, delete ALL nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Note:
    The difference between (E) 083. Remove Duplicates from Sorted List

'''

'''
Solution: 

** Note the case where no duplicate to jump
Time:O(n^2) easy solution
Space: O(1)
    
'''

class Solution:

    def deleteDuplicates(self, head):
        """
            :type head: ListNode
            :rtype: ListNode
            """

        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            # jump through dupliactes
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            # no duplicate to jump
            if prev.next == curr:
                prev = prev.next
            # jump to curr (last dup)'s next node
            else:
                prev.next = curr.next
            curr = curr.next

        return dummy.next
        
        
