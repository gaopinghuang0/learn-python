import unittest

# it's a little slower, but maybe due to unstable leetcode timer
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # idea: recursion
        # note that 1 <= k <= # of nodes
        # get sorted order and then get the kth element
        def helper(root, nodes):
            if root.left:
                helper(root.left, nodes)
            nodes.append(root.val)
            if root.right:
                helper(root.right, nodes)
        
        nodes = []
        helper(root, nodes)
        return nodes[k-1]

# beats 66.82%
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # idea: recursion
        # note that 1 <= k <= # of nodes
        # get sorted order and then get the kth element
        nodes = []
        def helper(root):
            if root.left:
                helper(root.left)
            nodes.append(root.val)
            if root.right:
                helper(root.right)
        
        helper(root)
        return nodes[k-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
