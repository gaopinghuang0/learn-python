import unittest

from itertools import combinations, chain
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(map(list, chain.from_iterable(combinations(nums,r) for r in range(len(nums)+1))))


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.subsets([1,2,3]), None)


if __name__ == "__main__":
  unittest.main()
