import unittest

# Brilliant solution
# Credit: https://discuss.leetcode.com/topic/18983/python-solution-accepted-o-n-time-o-1-space
class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # note: O(n) time, constant space complexity, and without division
    n = len(nums)
    p = 1
    output = []
    for i in range(0, n):   # left to right, get the product before nums[i]
      output += p,
      p *= nums[i]
    p = 1
    for i in range(n-1, -1, -1):  # right to left, get the product after nums[i]
      output[i] *= p
      p *= nums[i]
    return output



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
