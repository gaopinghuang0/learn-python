import unittest


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # idea: binary search since nums is a sorted array
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] > target:
                return i
            if nums[j] < target:
                return j + 1
            mid = (i+j)//2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    self.assertEqual(self.s.searchInsert([1,3,5,6], 5), 2)
    self.assertEqual(self.s.searchInsert([1,3,5,6], 2), 1)
    self.assertEqual(self.s.searchInsert([1,3,5,6], 7), 4)
    self.assertEqual(self.s.searchInsert([1,3,5,6], 0), 0)

if __name__ == "__main__":
  unittest.main()
