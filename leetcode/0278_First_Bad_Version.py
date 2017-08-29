import unittest


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
  return version > 10

class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    # binary search
    low = 1
    high = n
    while low <= high:
      mid = (low + high) // 2
      if isBadVersion(mid):
        high = mid - 1
      else:
        low = mid + 1
    return low



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.firstBadVersion(30), 11)


if __name__ == "__main__":
  unittest.main()
