import unittest


from itertools import combinations
class Solution(object):
  def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    d = {}
    for i in range(len(nums)+1):
      for x in combinations(nums, i):
        key = ''.join(map(str, x))  # since x will remain sorted
        if key not in d:
          d[key] = x

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
