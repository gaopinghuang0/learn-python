import unittest


class Solution(object):
  def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # note: subarray is continuous
    res, acc = 0, 0   # acc is accumulative sum so far
    acc_dict = {0: -1}  # acc : index
    for i, num in enumerate(nums):
      acc += num
      if acc not in acc_dict:
        acc_dict[acc] = i
      if acc - k in acc_dict:
        res = max(res, i - acc_dict[acc-k])
    return res
    


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.maxSubArrayLen([], 3), 0)
    self.assertEqual(self.s.maxSubArrayLen([1], 3), 0)
    self.assertEqual(self.s.maxSubArrayLen([3], 3), 1)
    self.assertEqual(self.s.maxSubArrayLen([3, 2], 3), 1)
    self.assertEqual(self.s.maxSubArrayLen([3, 2], 5), 2)
    self.assertEqual(self.s.maxSubArrayLen([3, 2], 4), 0)
    self.assertEqual(self.s.maxSubArrayLen([1,-1,5,-2,3], 3), 4)
    self.assertEqual(self.s.maxSubArrayLen([-2,-1,2,1], 1), 2)
    self.assertEqual(self.s.maxSubArrayLen([-2,-1,2,1], 0), 4)


if __name__ == "__main__":
  unittest.main()
