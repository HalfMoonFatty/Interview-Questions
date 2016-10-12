'''
Problem:

    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

    You must do this in-place without altering the nodes' values.

    For example,
    Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


'''
Solution:

step1. Find the middle point and slipt linked list from the middle. The head of the second list is slownext
step2. Reverse the second linked list. 有 Iterative 和 Recursive 两种解法，但是Python 的 recursive depth不能pass tests.
step3. Merge the first linked list and the second (reversed) linked list IN PLACE O(1) space. The merge function is kinda tricky.

'''


class Solution(object):
    def reorderList(self, head):
        """
            :type head: ListNode
            :rtype: void Do not return anything, modify head in-place instead.
            """

        def splitFromMid(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head2 = slow.next
            slow.next = None
            return head,head2


        '''
        # recursive reverse linked list function. but exceeded maxDepth
        def reverse(head):
            if not head.next:
                return head
            rest = head.next
            newhead = reverse(rest)
            rest.next = head
            head.next = None
            return newhead
        '''

        def reverse(head):
            last = None
            cur = head
            while cur:
                nextNode = cur.next
                cur.next = last
                last = cur
                cur = nextNode
            return last


        def merge(list1, list2):
            newhead = list1

            tail = list1
            list1 = list1.next
            while list2:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
                # if list 1 is not empty switch list1 with list2
                if list1:
                    list1, list2 = list2, list1
                    
            return newhead



        if not head or not head.next:
            return
        head1,head2 = splitFromMid(head)
        head2 = reverse(head2)
        merge(head1,head2)
        return
