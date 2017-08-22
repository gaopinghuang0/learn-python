import unittest


class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3:
      return False

    nums.sort()
    res = nums[0]+nums[1]+nums[2]
    if (target-res) == 0:
      return res

    size = len(nums)
    for i in xrange(size-2):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      left, right = i+1, size-1
      while left < right:
        s = nums[i]+nums[left]+nums[right]
        if (target - s) == 0:
          return s
        if abs(target-s) < abs(target-res):
          res = s
        if target < s:
          right -= 1
        elif target > s:
          left += 1
    return res


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    nums = [-1, 2, 1, -4]
    target = 1
    nums = [-1, 2, 1, -4]
    self.assertEqual(self.s.threeSumClosest(nums, target), 2)
    nums = [0, 0, 0]
    target = 1
    self.assertEqual(self.s.threeSumClosest(nums, target), 0)
    nums = [0,2,1,-3]
    target = 1
    self.assertEqual(self.s.threeSumClosest(nums, target), 0)
    nums = [1,-3,3,5,4,1]
    target = 1
    self.assertEqual(self.s.threeSumClosest(nums, target), 1)

if __name__ == "__main__":
  unittest.main()
