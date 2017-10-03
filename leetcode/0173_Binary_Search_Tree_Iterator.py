import unittest

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: use a queue to store the nodes
# whenever a node is popped out, it means its left child and itself have been popped out
# then try to insert the right child's left branch to the queue
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = []
        self.insertLeftBranch(root)

    def insertLeftBranch(self, node):
      while node:
        self.q.insert(0, node)
        node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0
        
    def next(self):
        """
        :rtype: int
        """
        node = self.q.pop(0)
        self.insertLeftBranch(node.right)
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


class TestSolution(unittest.TestCase):
  def setUp(self):
    pass

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    i, v = BSTIterator(root), []

    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
