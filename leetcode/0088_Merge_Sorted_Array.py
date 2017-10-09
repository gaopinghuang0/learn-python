import unittest


# credit: https://discuss.leetcode.com/topic/19513/beautiful-python-solution
class Solution(object):
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
      if nums1[m-1] >= nums2[n-1]:
        nums1[m+n-1] = nums1[m-1]
        m -= 1
      else:
        nums1[m+n-1] = nums2[n-1]
        n -= 1
    if n > 0:
      nums1[:n] = nums2[:n]



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
