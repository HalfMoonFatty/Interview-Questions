'''
Problem:

    Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
    If two nodes are in the same row and column, the order should be from left to right.

Examples:
    Given binary tree [3,9,20,null,null,15,7],
         3
        / \
       9  20
     /  \
    15   7
    return its vertical order traversal as:
    [
    [9],
    [3,15],
    [20],
    [7]
    ]

    Given binary tree [3,9,20,4,5,2,7],
        _3_
       /   \
      9    20
     / \   / \
    4   5 2   7
    return its vertical order traversal as:
    [
    [4],
    [9],
    [3,5,2],
    [20],
    [7]
    ]

'''

'''
Solution:

    import collections
    d = {2:3, 1:89, 4:5, 3:0}
    od = collections.OrderedDict(sorted(d.items()))
    print od
    >> OrderedDict([(1, 89), (2, 3), (3, 0), (4, 5)])
'''


from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
        if not root: return []
        
        mp = collections.defaultdict(list)
        q = deque()
        q.append((root, 0))
        while len(q) > 0:
            node, column = q.popleft()
            mp[column].append(node.val)
            if node.left: q.append((node.left, column-1))
            if node.right: q.append((node.right, column+1))


        ret = [mp[k] for k in sorted(mp)]
        return ret

    
    
# Follow-up: vertical print
def verticalOrder(root):

    # Find min and max distances with respect to root 
    def findMinMax(node, minimum, maximum, hd):
        if not node: return
        if hd < minimum[0]:
            minimum[0] = hd
        elif hd > maximum[0]:
            maximum[0] = hd
        findMinMax(node.left, minimum, maximum, hd-1)
        findMinMax(node.right, minimum, maximum, hd+1)
     

    def printVerticalLine(node, line_no, hd):
        if not node: return
        if hd == line_no:
            print node.data
        printVerticalLine(node.left, line_no, hd-1)
        printVerticalLine(node.right, line_no, hd+1)

     
    
    # Find min and max distances with respect to root
    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)
 
    # Iterate through all possible lines starting 
    # from the leftmost line and print nodes line by line
    for line_no in range(minimum[0], maximum[0]+1):
        printVerticalLine(root, line_no, 0)
