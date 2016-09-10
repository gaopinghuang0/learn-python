# 235_lowestCommonAncestor.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        while not p.val <= root.val <= q.val:
            root = root.left if q.val < root.val else root.right
        return root

x1 = TreeNode(2)
x2 = TreeNode(1)
x1.left = x2

print Solution().lowestCommonAncestor(x1, x1, x2).val