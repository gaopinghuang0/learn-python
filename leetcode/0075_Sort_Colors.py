import unittest


class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def sortColor(i, j, color):
      while True:
        while i < j and nums[i] == color:
          i += 1
        while i < j and nums[j] != color:
          j -= 1

        if i < j:
          nums[i], nums[j] = nums[j], nums[i]
        else:
          break
      return i
      
    n = len(nums)
    if n >= 2:
      i, j = 0, n-1
      # sort 0 first
      i = sortColor(i,j,0)
      # sort 1
      j = n - 1
      sortColor(i,j,1)



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
