import unittest


class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # idea: binary search to find the smallest value
    n = len(nums)
    low = 0
    high = n - 1
    while low < high:
      mid = (low + high) / 2
      if nums[mid] >= nums[low] and nums[mid] >= nums[high]:
        low = mid + 1
      else:
        high = mid
    rot = low
    print rot

    # pretend we rotate it back by idx % len(nums)
    low = rot
    high = n - 1 + rot
    while low <= high:
      mid = (low + high) / 2
      if nums[mid % n] > target:
        high = mid - 1
      elif nums[mid % n] < target:
        low = mid + 1
      else:
        return mid % n
    return -1



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
