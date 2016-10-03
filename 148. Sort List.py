'''
Problem:

    Sort a linked list in O(n log n) time using constant space complexity.

'''


'''
Solution: Recursion

The total time complexity is  O(nlgn);
But the space compexity is not constant
'''



class Solution(object):
    def __init_():
        self.headptr = None    # Global headptr to keep track the base case of sort function
   
   
    def sortList(self, head):

        if not head: return None
       
        len = 0    # pre-calculate length
        it = head
        while it:
            len += 1
            it = it.next
       
        self.headptr = head    # Global headptr
        newhead = self.sort(self.headptr,len)
        return newhead
   
   
   
    # Recursive function
    def sort(self, head, len):
        if len == 1:
            temp = self.headptr
            self.headptr = self.headptr.next    # 确保head每被访问一次，则向后移动一次
            temp.next = None                    # 尾节点需要为NULL，否则Merge函数没法使用
            return temp
       
        lefthead = self.sort(self.headptr,len/2)
        righthead = self.sort(self.headptr,len - len/2)
        newhead = self.merge(lefthead, righthead)
        return newhead
   
   
   
    def merge(self,left, right):
        dummyhead = ListNode(-1)
        prev = dummyhead
        while left and right:
            if left.val < right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next
       
        if not left and right is not None:
            prev.next = right
        if not right and left is not None:
            prev.next = left
        head = dummyhead.next
        return head
