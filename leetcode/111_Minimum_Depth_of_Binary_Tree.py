import unittest
from utils.TreeHelper import array_to_tree, print_in_level_order

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        root = array_to_tree([])
        self.assertEqual(self.s.minDepth(root), 0)
        root = array_to_tree([1, 2, None, 4, 5])
        print_in_level_order(root)
        self.assertEqual(self.s.minDepth(root), 3)




if __name__ == "__main__":
    unittest.main()
