import unittest

# optimize
class Solution(object):
  def increasingTriplet(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
      return False
    first = max(nums) + 1
    second = first

    for num in nums:
      if num <= first:  # guarantee that first is set to a number smaller than second if any
        first = num
      elif num <= second:
        second = num
      else:
        return True
    return False


# correct
class Solution(object):
  def increasingTriplet(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # O(t) time and O(1) space
    # idea: record the increasing trend, compare with the previous one
    # if the current one is higher, done; if not, replace the previous one with curr one
    n = len(nums)
    if n <= 2:
      return False
    inc_trend = None
    for i in range(n-1):
      a, b = nums[i], nums[i+1]
      if a < b:
        if inc_trend and inc_trend[1] < b:
          return True
        else:
          inc_trend = (a, b)
      elif a > b:
        if inc_trend and b > inc_trend[0]:
          inc_trend = (inc_trend[0], b)

    return False


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
