import unittest


class Solution(object):
  def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # idea: sort, 1D dp
    nums.sort()
    dp = [1] + [0] * target
    for i in range(1, target+1):
      for num in nums:
        if num > i: break
        elif num == i: dp[i] += 1
        else: dp[i] += dp[i-num]
    return dp[target]
        



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    print(self.s.combinationSum4([2,1,3], 4))


if __name__ == "__main__":
  unittest.main()
