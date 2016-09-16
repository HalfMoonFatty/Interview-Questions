'''
Problem:

    Given a binary tree, count the number of uni-value subtrees.
    A Uni-value subtree means all nodes of the subtree have the same value.

    For example:
    Given binary tree,
         5
        / \
       1   5
      / \   \
     5   5   5

     return 4.
'''


# Solution: countHelper function return 的 value是 True/False. count 在 input parameter, recursion 去更改这个值。


class Solution(object):
    def countUnivalSubtrees(self, root):


        def countHelper(root, count):

            # base case
            if not root:
                return True

            leftside = countHelper(root.left, count)
            rightside = countHelper(root.right, count)

            # only if both left and right are uni-value tree,
            # continue to compare root.val and left.val(if any) and right.val(if any)
            if leftside and rightside:
                if (not root.left and not root.right) or (root.left and root.right and root.val == root.right.val == root.left.val) or ((not root.left and root.val == root.right.val) or (not root.right and root.val == root.left.val)):
                    count[0] += 1
                    return True

            return False


        if not root:
            return 0

        count = [0]
        countHelper(root, count)
        return count[0]
