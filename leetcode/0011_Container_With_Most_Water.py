import unittest


class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    # area is determined by the lower edge
    # start from both ends, move inside
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
      max_area = max(max_area, min(height[left], height[right]) * (right - left))
      if height[left] < height[right]:
        # since left is lower, no matter how we move the right towards the left,
        # we cannot find a larger area,
        # thus it represents the max area so far,
        # in order to find a larger one, we can only move the left towards right
        left += 1
      else:
        right -= 1
    return max_area



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.maxArea([1, 1]), 1)
    self.assertEqual(self.s.maxArea([1, 3]), 1)
    self.assertEqual(self.s.maxArea([2, 1]), 1)
    self.assertEqual(self.s.maxArea([1, 3, 2]), 2)
    self.assertEqual(self.s.maxArea([3, 1, 2]), 4)
    self.assertEqual(self.s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


if __name__ == "__main__":
  unittest.main()
