'''
Problem:

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.
'''


class Solution(object):
    def closestValue(self, root, target):
        """
            :type root: TreeNode
            :type target: float
            :rtype: int
            """
        # record is [delta, node.val]
        def BShelper(root, target, record):
            if not root:
                return record
                
            delta = abs(root.val - target)
            if delta < record[0]:
                record = [delta, root.val]

            if root.val < target:
                record = BShelper(root.right, target, record)
            else:
                record = BShelper(root.left, target, record)
            return record


        if not root: return None
        record = [abs(root.val-target), root.val]
        return BShelper(root, target, record)[1]



# Pythonic coding

def closestValue(self, root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid: return a
    b = self.closestValue(kid, target)
    return min((b, a), key=lambda x: abs(target - x))
