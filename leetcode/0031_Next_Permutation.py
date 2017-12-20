import unittest


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if not self._nextPermutation(0, nums):
            self._reverse(0, nums)

    def _reverse(self, lo, nums):
        i, j = lo, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def _nextPermutation(self, pos, nums):
        if pos >= len(nums) - 1:  # only one element
            return False
        if self._nextPermutation(pos+1, nums):
            return True
        # nums[pos+1:] is in descending order
        if nums[pos] >= nums[pos+1]:
            return False
        else:
            # reverse nums[pos+1:]
            self._reverse(pos+1, nums)
            # switch nums[pos] with the num just larger than it
            i = pos + 1
            while i < len(nums):
                if nums[pos] < nums[i]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    break
                i += 1
            return True


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    nums = [1,2,3]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [1,3,2])
    nums = [3,2,1]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [1,2,3])
    nums = [1,1,5]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [1,5,1])
    nums = []
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [])
    nums = [1]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [1])
    nums = [1,2]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [2,1])
    nums = [3,2]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [2,3])
    nums = [4,8,7,6,6,3,1]
    self.s.nextPermutation(nums)
    self.assertEqual(nums, [6,1,3,4,6,7,8])


if __name__ == "__main__":
  unittest.main()
