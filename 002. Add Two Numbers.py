'''
Problem:
   
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
   
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''


'''
Solution: Recursion

    Linked List 注意 node 为 None 的情况，不能node.val
   
'''

class Solution:

    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        l=self.add2Num(l1,l2,carry)
        return l
   
   
    def add2Num(self,l1,l2,carry):
        val = 0
        if not l1 and not l2:
            return None if carry == 0 else ListNode(carry)
   
        val += l1.val if l1 else 0
        val += l2.val if l2 else 0
        val += carry
        
        carry = val/10
        val %= 10
        node = ListNode(val)
       
        arg1 = None if not l1 else l1.next
        arg2 = None if not l2 else l2.next
        node.next = self.add2Num(arg1,arg2,carry)    # Recursion
        return node

