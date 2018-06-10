

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# beats 8.81%
class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node.left:
                left_min, left_max = helper(node.left)
                self.res = min(abs(left_max - node.val), self.res)
            else:
                left_min, left_max = node.val, node.val
            if node.right:
                right_min, right_max = helper(node.right)
                self.res = min(abs(right_min - node.val), self.res)
            else:
                right_min, right_max = node.val, node.val
            return left_min, right_max
        
        self.res = float('inf')
        helper(root)
        return self.res

