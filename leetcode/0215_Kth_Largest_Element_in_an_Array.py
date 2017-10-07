import unittest


class Solution(object):
  def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return sorted(nums, reverse=True)[k] 


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    pass

if __name__ == "__main__":
  unittest.main()
