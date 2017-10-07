import unittest

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  def cloneGraph(self, node):
    def clone(node):
      new_node = UndirectedGraphNode(node.label)
      label_node_dict[node.label] = new_node
      for n in node.neighbors:
        if n.label not in label_node_dict:
          new_n = clone(n)
          new_node.neighbors.append(new_n)
        else:
          new_node.neighbors.append(label_node_dict[n.label])
      return new_node

    label_node_dict = {}
    if not node:
      return node
    return clone(node)



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
