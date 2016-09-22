'''
Problem:

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

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
            
