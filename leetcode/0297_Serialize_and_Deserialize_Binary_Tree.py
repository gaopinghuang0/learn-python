import unittest
from utils.TreeHelper import array_to_tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    def encode_preorder(node):
      if node:
        res.append(str(node.val))
        encode_preorder(node.left)
        encode_preorder(node.right)
      else:
        res.append('#')
    res = []
    encode_preorder(root)
    return ','.join(res)

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    def decode_preorder():
      x = next(res)
      if x == '#':
        return None
      node = TreeNode(int(x))
      node.left = decode_preorder()
      node.right = decode_preorder()
      return node

    res = iter(data.split(','))
    return decode_preorder()

    
class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Codec()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # root = array_to_tree([1,2,3,None,None,4,5])
    data = '1,2,#,#,3,4,#,#,5,#,#'
    root = self.s.deserialize(data)
    self.assertEqual(self.s.serialize(root), data)


if __name__ == "__main__":
  unittest.main()
