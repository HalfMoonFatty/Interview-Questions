'''
Problem:

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
    What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
    How would you optimize the kthSmallest routine?

Hint:
    Try to utilize the property of a BST.
    What if you could modify the BST node's structure?
    The optimal runtime complexity is O(height of BST).
'''


# note use result(obj) to store the kth elements
# dont just return value

class Solution(object):
    def kthSmallest(self, root, k):
        """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
        def inOrder(root, k, count, result):
            if not root or count[0] > k :
                return 

            inOrder(root.left, k, count, result)

            count[0] += 1
            if count[0] == k:
                result[0] = root.val

            inOrder(root.right, k, count, result)


        result = [0]
        inOrder(root, k, [0], result)
        return result[0]
        
        
