'''
Problem:

    Reverse a linked list from position m to n. Do it in-place and in one-pass.

    For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,
    return 1->4->3->2->5->NULL.

Note:
    Given m, n satisfy the following condition:
    1 ≤ m ≤ n ≤ length of list.

'''

'''
Solution :

    Set start to be the immediate node after prev.
    Rotate start, start.next(tmp).
    Repeat it for n - m times.
    Note, tmp.next should be set to prev.next not "start", because "start" it moving forward but prev is "fixed" which is forever the previous node of mth node.

    e.g. reverse 2,3,4 to 4,3,2
        pre  sta  tmp
         1 -> 2 -> 3 -> 4 -> 5

        pre       sta  tmp
         1 -> 3 -> 2 -> 4 -> 5

        pre       sta  tmp
         1 -> 4 -> 3 -> 2 -> 5

'''


class Solution(object):

    def reverseBetween(self, head, m, n):

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Note: mth node is 1-based index not 0-based index
        for i in range(m-1):
            prev = prev.next

        start = prev.next
        for i in range(n-m):
            tmp = start.next
            start.next = tmp.next
            tmp.next = prev.next  # not start
            prev.next = tmp

        return dummy.next
