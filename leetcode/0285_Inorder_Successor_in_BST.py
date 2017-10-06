import unittest

from utils.TreeHelper import array_to_BST, print_in_level_order, search_in_BST
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
          return None
        if p.right:
          # find the smallest one from right
          node = p.right
          while node:
            if node.left:
              node = node.left
            else:
              break
          return node

        prev = node = root
        while node:
          if node.val > p.val:
            prev = node
            node = node.left
          elif node.val == p.val:
            break
          else:
            node = node.right
        if p.val >= prev.val:  # the largest val is p
          return None
        return prev


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    root = array_to_BST([4, 2,3,1,5])
    print_in_level_order(root)
    p = search_in_BST(root, 2)
    print(self.s.inorderSuccessor(root, p).val)

    root = array_to_BST([0])
    p = search_in_BST(root, 0)
    print(self.s.inorderSuccessor(root, p).val)


if __name__ == "__main__":
  unittest.main()
