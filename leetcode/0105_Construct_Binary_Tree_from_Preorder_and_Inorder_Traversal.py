import unittest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# beats 11.01%
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # idea: divide and conquer
        # idx_dict = {val:i for i,val in enumerate(inorder)}
        if not preorder or not inorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        first = preorder[0]
        root = TreeNode(first)
        for i,val in enumerate(inorder):
            if val == first:
                break
        root.left = self.buildTree(preorder[1:i+1],inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
