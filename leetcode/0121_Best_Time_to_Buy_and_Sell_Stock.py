import unittest


class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # idea: two pointers. when a new min appears, the subsequent part should
    # compare with new min, not earlier one
    if len(prices) < 2:
      return 0
    res = 0
    cur_min = prices[0]
    for p in prices[1:]:
      if p < cur_min:
        cur_min = p
      else:
        res = max(res, p-cur_min)
    return res


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    prices = [7, 1, 5, 3, 6, 4]
    self.assertEqual(self.s.maxProfit(prices), 5)
    prices = [7, 6, 4, 3, 1]
    self.assertEqual(self.s.maxProfit(prices), 0)


if __name__ == "__main__":
  unittest.main()
