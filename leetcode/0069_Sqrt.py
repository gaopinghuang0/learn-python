import unittest


class Solution(object):
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    # idea: binary search
    if x <= 1:
      return x
    left, right = 1, x
    while True:
      mid = (left+right)/2
      if mid ** 2 > x:
        right = mid - 1
      elif (mid+1) ** 2 > x:
        return mid
      else:
        left = mid + 1


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
