import unittest

from utils.TreeHelper import array_to_tree, print_in_level_order
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    def preorder(node):
      if not node:
        return []
      res = []
      if not node.left and not node.right:
        return [str(node.val)]
      for path in preorder(node.left):
        res.append(str(node.val)+'->'+path)
      for path in preorder(node.right):
        res.append(str(node.val)+'->'+path)
      return res

    return preorder(root)

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    root = array_to_tree([1,2,3,None,5])
    # print_in_level_order(root)
    self.assertEqual(self.s.binaryTreePaths(root), ['1->2->5', '1->3'])


if __name__ == "__main__":
  unittest.main()
