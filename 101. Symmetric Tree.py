'''
Problem:

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree is symmetric:

            1
           / \
          2   2
         / \ / \
        3  4 4  3

    But the following is not:

            1
           / \
          2   2
           \   \
            3    3

Note:
    Bonus points if you could solve it both recursively and iteratively.
'''


# Solution 1: Recursive solution


class Solution(object):
    def isSymmetric(self, root):

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            else:
                return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
            
        return isMirror(root, root)




# Solution 2: Iterative Solution 64ms


from collections import deque
class Solution(object):

    def isSymmetric(self, root):

        if not root:
            return True

        q = deque()
        q.append(root)   
        q.append(root) 
        while len(q) > 0:
            t1 = q.popleft()
            t2 = q.popleft()
            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)

        return True
            
