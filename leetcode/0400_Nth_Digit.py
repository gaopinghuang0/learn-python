import unittest

# beats 22.00%
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea: 1-9: 9; 10-99: 90; 100-999: 900
        if n <= 9:
            return n
        n -= 1
        lookup = []
        total = 0
        i = 0
        while total < n:
            total += 9*(10**i)*(i+1)
            lookup.append(total)
            i += 1
        size = len(lookup)
        n_digits = size - 1
        prefix = n - lookup[n_digits-1]
        num = 1*10**n_digits + prefix//(n_digits+1)
        return int(str(num)[prefix % (n_digits+1)])

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.findNthDigit(11), 0)
    self.assertEqual(self.s.findNthDigit(3), 3)


if __name__ == "__main__":
  unittest.main()
