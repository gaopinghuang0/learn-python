import unittest

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
  def canAttendMeetings(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    # idea: sort first and compare the end of the prev interval
    # with the start of the next interval
    size = len(intervals)
    if size < 2:
      return True
    intervals.sort(key=lambda x: x.start)
    for i in range(1, size):
      prev = intervals[i-1]
      curr = intervals[i]
      if prev.end > curr.start:
        return False
    return True


def arr_to_interval_list(arr):
  return [Interval(a,b) for (a,b) in arr]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    intervals = arr_to_interval_list([[0, 30],[15, 20],[5, 10]])
    self.assertEqual(self.s.canAttendMeetings(intervals), False)
    intervals = arr_to_interval_list([[0, 5],[15, 20],[5, 10]])
    self.assertEqual(self.s.canAttendMeetings(intervals), True)


if __name__ == "__main__":
  unittest.main()
