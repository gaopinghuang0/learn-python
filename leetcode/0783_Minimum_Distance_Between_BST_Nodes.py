

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# beats 62.63%
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: recursive, compare the root with the largest of left branch (the rightmost node)
        # and with the least of the right branch (the leftmost node)
        res = float('inf')
        if root.left:
            left_min = self.minDiffInBST(root.left)
            node = root.left
            while node.right:
                node = node.right
            res = min(abs(root.val - node.val), left_min)
        if root.right:
            right_min = self.minDiffInBST(root.right)
            node = root.right
            while node.left:
                node = node.left
            res = min(abs(root.val - node.val), right_min, res)

        return res