import unittest

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # n could be positive and negative
        def _myPow(n):
          if n in d:
            return d[n]
          a = n // 2
          b = n - a
          if a in d:
            left = d[a]
          else:
            left = _myPow(a)
            d[a] = left

          if b in d:
            right = d[b]
          else:
            right = _myPow(b)
            d[b] = right

          return left * right

        if n == 0:
          return 1.0
        if x == 0:
          return 0.0
        d = {1: x, 2: x*x, 3: x*x*x}
        if n < 0:
          return 1 / _myPow(-n)
        return _myPow(n)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertTrue(self.s.myPow(8.88023, 3) - 700.28148 < 0.0001)
    self.assertTrue(self.s.myPow(8.88023, -3) - 1/700.28148 < 0.0001)


if __name__ == "__main__":
  unittest.main()
