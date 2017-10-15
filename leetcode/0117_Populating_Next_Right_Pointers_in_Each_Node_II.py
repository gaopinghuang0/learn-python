import unittest


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
      # note: constant extra space
      # idea: level-order traverse, parent is the pointer in the parent level, node is the child level 
      dummy = node = TreeLinkNode(0)
      parent = root
      while parent:
        node.next = parent.left
        if node.next:
          node = node.next
        node.next = parent.right
        if node.next:
          node = node.next
        parent = parent.next
        if not parent:
          node = dummy
          parent = dummy.next

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
