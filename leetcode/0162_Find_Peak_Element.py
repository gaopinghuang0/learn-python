import unittest

# beats 47.79%
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        peak = nums[0]
        for i in range(1, n):
            if peak < nums[i]:
                peak = nums[i]
            else:
                return i - 1
        return n - 1


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # nums = []  ==> invalid
    nums = [1]
    self.assertEqual(self.s.findPeakElement(nums), 0)
    nums = [1,2]
    self.assertEqual(self.s.findPeakElement(nums), 1)
    nums = [1,2,3,1]
    self.assertEqual(self.s.findPeakElement(nums), 2)
    nums = [1,2,3,4]
    self.assertEqual(self.s.findPeakElement(nums), 3)


if __name__ == "__main__":
  unittest.main()
