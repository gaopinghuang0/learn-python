import unittest


class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n)
    # idea: use a dict to store num, for each num, check whether num-1 or num+1 is in the dict
    d = {num: True for num in nums}
    ans = 0
    while d:
      for num in d:
        i = 1
        t = num
        del d[t]
        while t - 1 in d:
          i += 1
          t -= 1
          del d[t]
        t = num
        while t + 1 in d:
          i += 1
          t += 1
          del d[t]
        ans = max(i, ans)
        break
    return ans




class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
