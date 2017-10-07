import unittest


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
  def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    start = newInterval.start
    end = newInterval.end

    left = [i for i in intervals if i.end < start]
    right = [i for i in intervals if i.start > end]

    # check if we should merge
    if len(left) + len(right) < len(intervals):
      start = min(start, intervals[len(left)].start)
      end = max(end, intervals[-len(right)-1].end)

    return left + [Interval(start, end)] + right



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
