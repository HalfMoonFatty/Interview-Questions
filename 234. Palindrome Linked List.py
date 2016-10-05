'''
Problem:

    Given a singly linked list, determine if it is a palindrome.

Follow up:

    Could you do it in O(n) time and O(1) space?
    
'''


'''
Solution 1: Iterative Solution

Time: O(n)
Space: O(n)
'''

class Solution(object):

    def isPalindrome(self, head):

        def checkPalin(start,end,mp):
            length = 1
            while end.next:
                mp[end.next] = end
                end = end.next
                length += 1

            for i in range(length/2):
                if start.val == end.val:
                    start = start.next
                    end = mp[end]
                else:
                    return False
            return True


        if not head or not head.next:
            return True

        return checkPalin(head,head,{})




'''
Solution 2: Optimal
Time: O(n)
Space: O(1)

1. find the middle.
2. reverse half of the list (reverse the latter half - more comprehensible).
3. easily check for palindromic-ness as if it's a double-link list.
4. restore the reversed half
'''

class Solution(object):

    def isPalindrome(self, head):

        def reverseLL(head):
            if not head or not head.next:
                return

            reverseLL(head.next)
            head.next.next = head
            head.next = None
            return


        #if len is 0 or 1
        if not head or not head.next:
            return True

        # step 1. find the middle node
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if not fast.next: last = fast
        else: last = fast.next


        # step 2. reverse the second half; connect it to the first half
        reverseLL(slow.next)
        slow.next = last


        # step 3. check palindrome
        first = head
        second = slow.next
        result = True
        while second:
            if first.val != second.val:
                result = False
                break
            else:
                first = first.next
                second = second.next

        # step 4. restore the linked list
        last.next = None
        reverseLL(slow.next)

        return result







'''
* Solution 3: Recursive Solution

Time: O(n)
Space Complexity: O(n)
'''

class Solution(object):
    def __init__(self):
        self.cur = None

    def isPalindrome(self, head):

        def checkPalin(tail):
            if not tail:
                return True
            isPalind = checkPalin(tail.next) and (self.cur.val == tail.val)
            self.cur = self.cur.next
            return isPalind

        self.cur = head
        return checkPalin(head)

