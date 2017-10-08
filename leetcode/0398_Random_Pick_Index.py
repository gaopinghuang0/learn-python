import unittest


# Reservoir Sampling
# Credit: https://discuss.leetcode.com/topic/58301/simple-reservoir-sampling-solution
from random import randint
class Solution(object):

  def __init__(self, nums):
    """
    :type nums: List[int]
    :type numsSize: int
    """
    self.nums = nums

  def pick(self, target):
    """
    :type target: int
    :rtype: int
    """
    count = 0
    result = -1
    for i, n in enumerate(self.nums):
      if n != target:
        continue
      if randint(0, count) == 0:
        result = i
      count += 1
    return result
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
