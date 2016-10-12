'''
Problem:

Given a non-negative number represented as a singly linked list of digits, plus one to the number.

     The digits are stored such that the most significant digit is at the head of the list.

Example:

    Input:
    1->2->3

    Output:
    1->2->4

'''


class Solution(object):
    def plusOne(self, head):

        def recPlusOne(itr):
            if not itr.next:
                val = (itr.val+1)%10
                carry = (itr.val+1)/10
                itr.val = val
                return carry
            else:
                carry = recPlusOne(itr.next)
                val = (itr.val+carry)%10
                carry = (itr.val+carry)/10
                itr.val = val
                return carry


        if not head: return None

        dummy = ListNode(0)
        dummy.next = head
        recPlusOne(dummy)

        return dummy if dummy.val > 0 else dummy.next
