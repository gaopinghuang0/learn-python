import unittest


class Solution(object):
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # idea: dynamic programming
    n = len(s)
    if len(s) == 0:
      return 0

    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 0 if int(s[0]) == 0 else 1
    for i in range(2, n+1):
      first = int(s[i-1])
      second = int(s[i-2: i])
      if first >= 1 and first <= 9:
        dp[i] += dp[i-1]
      if second >= 10 and second <= 26:
        dp[i] += dp[i-2]
    return dp[n]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.numDecodings(''), 0)
    self.assertEqual(self.s.numDecodings('1'), 1)
    self.assertEqual(self.s.numDecodings('10'), 1)
    self.assertEqual(self.s.numDecodings('12'), 2)
    self.assertEqual(self.s.numDecodings('123'), 3)
    self.assertEqual(self.s.numDecodings('01'), 0)
    self.assertEqual(self.s.numDecodings('1001'), 0)


if __name__ == "__main__":
  unittest.main()
