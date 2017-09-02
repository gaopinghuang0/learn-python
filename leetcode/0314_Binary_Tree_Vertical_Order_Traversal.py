import unittest

from utils.TreeHelper import TreeNode, array_to_tree, print_in_level_order

from collections import defaultdict, deque
class Solution(object):
  def verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    # idea: level-order transverse. Set root as column 0, column of left is root-1
    # column of right is root + 1

    column_dict = defaultdict(list)
    if not root:
      return []
    stack = deque()
    stack.append((root,0))
    while len(stack):
      node, x = stack.popleft()
      column_dict[x].append(node.val)
      if node.left:
        stack.append((node.left, x-1))
      if node.right:
        stack.append((node.right, x+1))
    
    return [column_dict[col_index] for col_index in sorted(column_dict.keys())]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    tree = []
    res = []
    self.assertEqual(self.s.verticalOrder(array_to_tree(tree)), res)

    tree = [None]
    res = []
    self.assertEqual(self.s.verticalOrder(array_to_tree(tree)), res)

    tree = [3,9,20,None,None,15,7]
    res = [
      [9],
      [3,15],
      [20],
      [7]
    ]
    self.assertEqual(self.s.verticalOrder(array_to_tree(tree)), res)

    tree = [3,9,8,4,0,1,7]
    res = [
      [4],
      [9],
      [3,0,1],
      [8],
      [7]
    ]
    self.assertEqual(self.s.verticalOrder(array_to_tree(tree)), res)

    tree = [3,9,8,4,0,1,7,None,None,None,2,5]
    res = [
      [4],
      [9,5],
      [3,0,1],
      [8,2],
      [7]
    ]
    self.assertEqual(self.s.verticalOrder(array_to_tree(tree)), res)


if __name__ == "__main__":
  unittest.main()
