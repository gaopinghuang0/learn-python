import unittest


from collections import defaultdict
class Solution(object):
  def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    pre, suc = defaultdict(set), defaultdict(set)
    for a, b in prerequisites:
      pre[a].add(b)
      suc[b].add(a)
    free = set(range(numCourses)) - set(pre)
    order = []
    while free:
      b = free.pop()
      order.append(b)
      for a in suc[b]:
        pre[a].discard(b)
        if not pre[a]:
          free.add(a)
    return order if len(order) == numCourses else []


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
