import unittest


# idea from Discuss, beats 28.34%
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # idea from Discuss
        # https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
        # reverse sort, put small half in the even index (0, 2, ...), large half in the odd index
        nums.sort()
        half = len(nums[::2]) - 1
        # one way
        # nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        # or
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)

    self.s.wiggleSort(list(range(10)))
    self.s.wiggleSort(list(range(11)))
    self.s.wiggleSort(list(range(12)))
    self.s.wiggleSort(list(range(13)))


if __name__ == "__main__":
  unittest.main()
