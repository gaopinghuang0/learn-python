import unittest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# beats 9.52%
class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        # idea: recursive
        if not root:
            return [None, None]
        if root.val > V:  # root belongs to the right subtree
            left_sub, right_sub = self.splitBST(root.left, V)
            root.left = right_sub
            return [left_sub, root]
        else:
            left_sub, right_sub = self.splitBST(root.right, V)
            root.right = left_sub
            return [root, right_sub]



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
