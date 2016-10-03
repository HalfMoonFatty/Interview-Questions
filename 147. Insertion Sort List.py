'''
Problem:

     Sort a linked list using insertion sort.

'''


'''
Solution 1:

    Step 1. Iterate throught the list to find the rule breaker - curr.next
    Step 2. Find the insertion position using prev itr
    Step 3. Insert curr.next between prev and prev.next

'''

class Solution(object):
   
    def insertionSortList(self, head):
       
        if not head: return None
       
        dummy = ListNode(0)
        dummy.next = head
        curr = head
       
        while curr.next:
           
            # find the rule breaker - curr.next
            if curr.next.val < curr.val:
               
                # find the insertion position using prev itr
                prev = dummy
                while prev.next and prev.next.val < curr.next.val:
                    prev = prev.next
               
                # insert curr.next between prev and prev.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
           
            else:
                curr = curr.next
       
        return dummy.next
