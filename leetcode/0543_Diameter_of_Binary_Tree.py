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
        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            d = left + right + 1          
            if d > self.res:
                self.res = d
            return 1 + max(left, right)

        self.res = 0
        depth(root)
        return self.res



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
