import unittest


class Solution(object):
  def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if not nums or sum(nums) < s:
      return 0
    n = len(nums)
    i, j = 0, -1
    count = 0
    ans = n
    while i < n:
      if count < s:
        if j < n - 1:
          j += 1
          count += nums[j]
        else:
          break
      else:
        while count >= s:
          ans = min(ans, j-i+1)
          count -= nums[i]
          i += 1
    return ans


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
