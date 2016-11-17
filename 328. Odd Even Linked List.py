'''
Problem:

    Given a singly linked list, group all odd nodes together followed by the even nodes.
    Please note here we are talking about the node number and not the value in the nodes.
    You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
    Given 1->2->3->4->5->NULL,
    return 1->3->5->2->4->NULL.

Note:
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...

'''



class Solution(object):
    def oddEvenList(self, head):

        if not head:
            return None

        odd,even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head
