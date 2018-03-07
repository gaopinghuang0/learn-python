import unittest


# beats 53.62%
from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea: use a counter, find pair of even chars
        res = 0
        count = defaultdict(int)
        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        for key, val in count.items():
            if val % 2 == 1:
                return res + 1
        return res

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
