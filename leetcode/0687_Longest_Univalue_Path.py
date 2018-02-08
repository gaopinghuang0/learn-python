# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea from Discuss, beats 15.46%
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: recursive
        self.largest = 0
        val, max_len = self.findLongest(root)
        return self.largest

    def findLongest(self, node):
        if not node:
            return 0

        left_count = self.findLongest(node.left)
        right_count = self.findLongest(node.right)
        left = (left_count+1) if node.left and node.val == node.left.val else 0
        right = (right_count+1) if node.right and node.val == node.right.val else 0
        self.largest = max(self.largest, left+right)
        return max(left, right)





