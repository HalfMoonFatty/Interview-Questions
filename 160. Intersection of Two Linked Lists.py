'''
Problem:

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                    c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
     If the two linked lists have no intersection at all, return null.
     The linked lists must retain their original structure after the function returns.
     You may assume there are no cycles anywhere in the entire linked structure.
     Your code should preferably run in O(n) time and use only O(1) memory.

'''

# Time:  O(M+N)
# Space: O()

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
            :type head1, head1: ListNode
            :rtype: ListNode
            """

        pa,pb = headA,headB
        lenA, lenB = 0, 0
        while pa:
            lenA += 1
            pa = pa.next
        while pb:
            lenB += 1
            pb = pb.next

        pa,pb = headA,headB

        if lenA > lenB:
            diff = lenA-lenB
            for i in range(diff):
                pa = pa.next
        elif lenB > lenA:
            diff = lenB-lenA
            for i in range(diff):
                pb = pb.next

        while pa != pb:
            pa = pa.next
            pb = pb.next
        return pa
