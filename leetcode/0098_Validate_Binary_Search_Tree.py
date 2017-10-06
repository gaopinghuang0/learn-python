import unittest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
          return True
        if root.left:
          node = root.left
          while node:
            if node.val >= root.val:
              return False
            node = node.right
          if not self.isValidBST(root.left):
            return False
        if root.right:
          node = root.right
          while node:
            if node.val <= root.val:
              return False
            node = node.left
          if not self.isValidBST(root.right):
            return False
        return True


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    # Such as self.assertEqual, self.assertTrue
    # [] -> True
    # [0] -> True
    # [2,3] -> True
    # [10,5,15,null,null,6,20]  -> False
    # self.assertEqual(self.s.isValidBST([2,3]), None)
    pass

if __name__ == "__main__":
  unittest.main()
