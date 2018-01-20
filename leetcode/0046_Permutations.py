import unittest

# beats 58.61%
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        first = nums[0]
        res = []
        for arr in self.permute(nums[1:]):
            for i in range(len(arr)+1):
                res.append(arr[:i]+[first]+arr[i:])
        return res

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
