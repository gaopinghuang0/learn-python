import unittest


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.q = nestedList

    def next(self):
        """
        :rtype: int
        """
        return self.q.pop(0).getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.q:
          return False

        node = self.q[0]
        if node.isInteger():
          return True
        node = self.q.pop(0)
        self.q = node.getList() + self.q
        return self.hasNext()
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  # def test_method(self):
  #   # Such as self.assertEqual, self.assertTrue
  #   self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
