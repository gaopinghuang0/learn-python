import unittest


class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # idea: two-pointer
    if not nums:
      return 0

    i,j = 0,1
    n = len(nums)
    last = nums[i]
    while j < n:
      if last < nums[j]:
        i += 1
        nums[i] = nums[j]
        last = nums[i]
      j += 1
    return i+1


    


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.removeDuplicates([]), 0)
    self.assertEqual(self.s.removeDuplicates([1]), 1)
    self.assertEqual(self.s.removeDuplicates([1,1]), 1)
    self.assertEqual(self.s.removeDuplicates([1,2]), 2)
    self.assertEqual(self.s.removeDuplicates([1,1,2]), 2)
    self.assertEqual(self.s.removeDuplicates([1,1,2,2,3]), 3)
    self.assertEqual(self.s.removeDuplicates([1,2,2,2,3]), 3)


if __name__ == "__main__":
  unittest.main()
