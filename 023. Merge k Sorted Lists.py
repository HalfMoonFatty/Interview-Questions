'''
Problem:

    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
   
'''

'''
Time: O(n*logk)
Space: O(logk)
n is number of nodes
'''


import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        dummyHead = ListNode(-1)
        itr = dummyHead
        
        heap = []
        for i in range(len(lists)):
            if lists[i]: # Note
                heapq.heappush(heap,(lists[i].val,i))
                lists[i] = lists[i].next
        
        while len(heap):
            elem = heapq.heappop(heap)
            val, ind = elem[0],elem[1]
            itr.next = ListNode(val)
            itr = itr.next # Note
            if lists[ind]: # Note
                heapq.heappush(heap,(lists[ind].val,ind))
                lists[ind] = lists[ind].next
                
        return dummyHead.next
        
        
        
