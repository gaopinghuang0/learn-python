import unittest

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _diameter(node):
            if not node:
                return 0
            d = longest_length(node.left) + longest_length(node.right)
            if d > self.res:
                self.res = d
            _diameter(node.left)
            _diameter(node.right)
        def longest_length(node):
            if not node:
                return 0
            return max(longest_length(node.left), longest_length(node.right)) + 1

        if not root:
            return 0
        self.res = 0
        _diameter(root)
        return self.res



class TestSolution(unittest.TestCase):
  def setUp(self):
    pass

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
