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

        def compareLR(left, right):
            if not left and not right:
                return True
            elif left and right and left.val == right.val:
                return compareLR(left.left, right.right) and compareLR(left.right, right.left)
            else:
                return False


        if not root:
            return True
        else:
            return compareLR(root.left, root.right)





# Solution 2: Iterative Solution 64ms


from collections import deque
class Solution(object):

    def isSymmetric(self, root):

        if not root:
            return True

        # init q1 and q2
        q1 = deque()
        q2 = deque()
        q1.append(root.left)    # q1 - left, right
        q2.append(root.right)   # q2 - right, left (mirror)

        # pop both queue
        while len(q1) > 0 and len(q2) > 0:
            l = q1.popleft()
            r = q2.popleft()
            if not l and not r:
                continue
            elif not l or not r:
                return False
            elif l.val != r.val:
                return False

            # q1 - left, right
            q1.append(l.left)
            q1.append(l.right)
            # q2 - right, left (mirror)
            q2.append(r.right)
            q2.append(r.left)

        return True

