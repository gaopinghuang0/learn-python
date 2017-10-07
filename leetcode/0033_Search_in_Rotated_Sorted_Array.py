import unittest


class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # idea: binary search
    n = len(nums)
    if not n:
      return -1

    low, high = 0, n-1
    while low < high:
      mid = (low + high) / 2
      cur = nums[mid]
      if cur == target:
        return mid

      if cur >= nums[low]:  # left side is sorted
        if target >= nums[low] and cur >= target:
          high = mid - 1
        else:
          low = mid + 1
      else:  # right side is sorted
        if target >= cur and target <= nums[high]:
          low = mid + 1
        else:
          high = mid - 1
    return high if nums[high] == target else -1


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
