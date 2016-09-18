'''
Problem:

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''


class Solution(object):
    def sortedListToBST(self, head):
        """
            :type head: ListNode
            :rtype: TreeNode
            """

        start = head
        # note: 2 base cases
        if not start: return None
        if not start.next: return TreeNode(start.val)    

        # use fast and slow poiters to find the mid point
        slow, fast = start, start
        prev = ListNode(-10000)     # dummy node
        prev.next = start
        while fast and fast.next:
            fast = fast.next.next   
            slow = slow.next        # slow reaches mid
            prev = prev.next

        # start->...->prev-> mid(slow) ->start2->...->None
        # Break the list into 2 lists
        prev.next = None
        start2 = slow.next

        root = TreeNode(slow.val)    
        root.left = self.sortedListToBST(start)
        root.right = self.sortedListToBST(start2)
        
    return root
