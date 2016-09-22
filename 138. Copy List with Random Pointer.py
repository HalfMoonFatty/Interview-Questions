'''
Problem:

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

'''



# Solution 1: Time O(n); Space O(n)

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        
        mp = {}
        itr = head
        while itr:
            cpitr = None
            if mp.has_key(itr):
                cpitr = mp[itr]
            else:
                cpitr = RandomListNode(itr.label)
                mp[itr] = cpitr
            
            cpnext = None
            if itr.next:
                if mp.has_key(itr.next):
                    cpnext = mp[itr.next]
                else:
                    cpnext = RandomListNode(itr.next.label)
                    mp[itr.next] = cpnext
            
            cprand = None
            if itr.random:
                if mp.has_key(itr.random):
                    cprand = mp[itr.random]
                else:
                    cprand = RandomListNode(itr.random.label)
                    mp[itr.random] = cprand
        
        
            cpitr.next = cpnext
            cpitr.random = cprand
            itr = itr.next
        
        return mp[head]
            



# Solution 2: Time O(n); Space O(1)

class Solution(object):
    def copyRandomList(self, head):
        """
            :type head: RandomListNode
            :rtype: RandomListNode
            """
        if not head:
            return None

        # first iteration: copy the original linked list
        itr = head
        while itr:
            copy = RandomListNode(itr.label)
            copy.next = itr.next
            itr.next = copy
            itr = itr.next.next

        # second iteration: copy the random pointer in the original linked list
        itr = head
        while itr:
            if itr.random:
                copy = itr.next
                copy.random = itr.random.next
            itr = itr.next.next;

        # third iteration: restore the original list and extract the new list
        itr = head
        cpitr, newHead = head.next, head.next
        while cpitr:
            itr.next = cpitr.next
            itr = itr.next
            if not itr:
                break
            cpitr.next = itr.next
            cpitr = cpitr.next

        return newHead
