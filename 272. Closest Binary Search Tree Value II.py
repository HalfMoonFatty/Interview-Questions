'''
Problem:

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:
1. Consider implement these two helper functions:
        - getPredecessor(N), which returns the next smaller node to N.
        - getSuccessor(N), which returns the next larger node to N.
2. Try to assume that each node has a parent pointer, it makes the problem much easier.
3. Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
4. You would need two stacks to track the path in finding predecessor and successor node separately.
'''



class Solution(object):
    def closestKValues(self, root, target, k):
        """
            :type root: TreeNode
            :type target: float
            :type k: int
            :rtype: List[int]
            """
            
        def initSuccessor(root, target, suc):
            while root:
                if root.val > target:
                    suc.append(root)
                    root = root.left
                else:
                    root = root.right
            return


        def initPredecessor(root, target, pred):
            while root:
                # note: add node whose value equals to target to the pred stack
                if root.val <= target:
                    pred.append(root)
                    root = root.right
                else:
                    root = root.left
            return


        def getNextSuccessor(suc):
            cur = suc.pop()
            ret = cur.val
            cur = cur.right
            while cur:
                suc.append(cur)
                cur = cur.left
            return ret


        def getNextPredecessor(pred):
            cur = pred.pop()
            ret = cur.val
            cur = cur.left
            while cur:
                pred.append(cur)
                cur = cur.right
            return ret



        if not root:
            return None

        result = []
        suc, prev = [], []
        # pred and suc stack initialization
        initPredecessor(root, target, pred)
        initSuccessor(root, target, suc)

        for i in range(k):
            # pay attention to the corner case
            if not suc:
                result.append(getNextPredecessor(pred))
            elif not pred:
                result.append(getNextSuccessor(suc))
            else:
                if abs(target-suc[-1].val) < abs(target-pred[-1].val):
                    result.append(getNextSuccessor(suc))
                else:
                    result.append(getNextPredecessor(pred))
        return result
