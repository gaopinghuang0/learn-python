import unittest

# beats 54.90%
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # idea: first sort
        citations = sorted(citations, reverse=True)
        for i, c in enumerate(citations, 1):
            if i > c:
                return i-1
        return len(citations)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    citations = [3, 0, 6, 1, 5]
    self.assertEqual(self.s.hIndex(citations), 3)
    citations = [3, 0, 6, 1, 5, 5, 2, 8]
    self.assertEqual(self.s.hIndex(citations), 4)
    citations = [3, 6]
    self.assertEqual(self.s.hIndex(citations), 2)
    citations = [0]
    self.assertEqual(self.s.hIndex(citations), 0)
    


if __name__ == "__main__":
  unittest.main()
