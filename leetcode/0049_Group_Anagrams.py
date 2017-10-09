import unittest


class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    from collections import defaultdict
    d = defaultdict(list)
    for x in strs:
      key = ''.join(sorted(x))
      d[key].append(x)

    return d.values()


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
