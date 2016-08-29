'''
Problem:

	Merge two sorted linked lists and return it as a new list.
	The new list should be made by splicing together the nodes of the first two lists.
'''

# Note: after the merging, remember to connect the rest of the lists

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummynode = ListNode(-1)
        prev = dummynode
        
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                prev.next = l2
                prev = prev.next
                l2 = l2.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
            
        return dummynode.next