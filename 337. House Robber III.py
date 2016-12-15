'''
Problem:


The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. The thief realized that all houses in this place forms a binary tree. 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.



Example 1:
          3
         / \
        2   3
         \   \
          3   1
    Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
            3
           / \
          4   5
         / \   \
        1   3   1
    Maximum amount of money the thief can rob = 4 + 5 = 9.

'''



'''
Step I -- Recursion
'''

public int rob(TreeNode root) {
    if (root == null) {
        return 0;
    }

    int val = 0;

    if (root.left != null) {
        val += rob(root.left.left) + rob(root.left.right);
    }

    if (root.right != null) {
        val += rob(root.right.left) + rob(root.right.right);
    }

    return Math.max(val + root.val, rob(root.left) + rob(root.right));
}



'''
Step II -- use a hash map to record the results for visited subtrees (overlapping of the subproblems)

'''

public int rob(TreeNode root) {
    Map<TreeNode, Integer> map = new HashMap<>();
    return robSub(root, map);
}

private int robSub(TreeNode root, Map<TreeNode, Integer> map) {
    if (root == null) return 0;
    if (map.containsKey(root)) return map.get(root);

    int val = 0;

    if (root.left != null) {
        val += robSub(root.left.left, map) + robSub(root.left.right, map);
    }

    if (root.right != null) {
        val += robSub(root.right.left, map) + robSub(root.right.right, map);
    }

    val = Math.max(val + root.val, robSub(root.left, map) + robSub(root.right, map));
    map.put(root, val);

return val;
}



'''
Step III -- Think one step back

For each tree root, there are two scenarios: it is robbed or is not. rob(root) does not distinguish between these two cases, 
so "information is lost as the recursion goes deeper and deeper", which resulted in repeated subproblems.

Redefine rob(root) as a new function which will return an array of two elements:
the 1st element denotes the maximum amount of money robbed if root is robbed = root.val + rob(root.left)[1] + rob(root.right)[1]
the 2nd element denotes the maximum amount of money that can be robbed if root is NOT robbed = max(leftVals[0],leftVals[1]) + max(rightVals[0],rightVals[1])


dfs all the nodes of the tree, each node return two number, int[] num, 
num[0] is the max value while rob this node, num[1] is max value while not rob this value. 

'''

class Solution(object):
    def rob(self, root):

        def dfs(root):
            if not root: return [0,0]
            
            leftVals = dfs(root.left)
            rightVals = dfs(root.right)

            res = [0,0]
            # root is robbed and not rob the nodes of root.left and root.right
            res[0] = root.val + leftVals[1] + rightVals[1]
            # root is not robbed and we are free to rob the left and right subtrees.
            res[1] = max(leftVals[0],leftVals[1]) + max(rightVals[0],rightVals[1])
            return res

        result = dfs(root)
        return max(result[0],result[1])
