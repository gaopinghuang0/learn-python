import unittest


class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    from collections import defaultdict, Counter
    d = defaultdict(list)
    for x in strs:
      d[frozenset(x)].append(x)
    # if x is in diff set, they must not be anagrams
    # but if they are in the same set, they may not be anagrams
    ans = []
    for group in d.values():
      keys = []
      temp = defaultdict(list)
      for x in group:
        c = Counter(x)
        if c in keys:
          idx = keys.index(c)
          temp[idx].append(x)
        else:
          keys.append(c)
          temp[len(keys)-1].append(x)
      ans += temp.values()

    return ans


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
