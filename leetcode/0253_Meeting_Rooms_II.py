import unittest

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from heapq import *
class Solution(object):
  def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    size = len(intervals)
    if size < 2:
      return size
    intervals.sort(key=lambda x: x.start)

    heap = []
    heappush(heap, intervals[0].end)
    for i in intervals[1:]:
      if i.start >= heap[0]:
        heappushpop(heap, i.end)
      else:
        heappush(heap, i.end)
    return len(heap)


def arr_to_interval_list(arr):
  return [Interval(a,b) for (a,b) in arr]

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    intervals = arr_to_interval_list([[0, 30],[15, 20],[5, 10]])
    self.assertEqual(self.s.minMeetingRooms(intervals), 2)

    intervals = arr_to_interval_list([[0, 5],[15, 20],[5, 10]])
    self.assertEqual(self.s.minMeetingRooms(intervals), 1)

    intervals = arr_to_interval_list([[0, 35],[15, 20],[20, 50]])
    self.assertEqual(self.s.minMeetingRooms(intervals), 2)

    intervals = arr_to_interval_list([[0, 35],[15, 20],[10, 50]])
    self.assertEqual(self.s.minMeetingRooms(intervals), 3)


if __name__ == "__main__":
  unittest.main()
