import unittest

# A great blog post with detailed explanations
# https://briangordon.github.io/2014/08/the-skyline-problem.html
# Credit: adapted from https://discuss.leetcode.com/topic/34119/10-line-python-solution-104-ms
from heapq import *
class Solution(object):
  def getSkyline(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    # critical points: all left corners + set comprehension of right corners
    crit_points = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
    ans = [[0, 0]]  # [x, H]
    hp = [(0, float('inf'))]  # (negH, R) to represent rectanges
    # use negH because heapq is min-heap but we need to find max height, so store negH
    for x, negH, R in crit_points:
      while x >= hp[0][1]:  # remove all rectanges on the left of x
        heappop(hp)
      if negH:  # add rectangle
        heappush(hp, (negH, R))
      if ans[-1][1] != -hp[0][0]:  # store when max_height changes
        ans += [x, -hp[0][0]],  # faster than append()
    return ans[1:]


# Below is Memory Error because n is > INT_MAX
# class Solution(object):
#   def getSkyline(self, buildings):
#     """
#     :type buildings: List[List[int]]
#     :rtype: List[List[int]]
#     """
#     # idea: DP, use 1D array to store highest high
#     if not buildings:
#       return buildings
#     n = max(b[1] for b in buildings) + 1
#     dp = [0]*n
#     for b in buildings:
#       for i in range(b[0], b[1]):  # ignore the right most point of building
#         dp[i] = max(dp[i], b[2])
#     prev = 0
#     ans = []
#     for i, h in enumerate(dp):
#       if prev != h:  # and overlap
#         prev = h
#         ans.append([i,h])
#     return ans
    

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
