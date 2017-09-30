import unittest

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
  def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    size = len(intervals)
    if size < 2:
      return intervals
    intervals.sort(key=lambda x: x.start)
    res = [intervals[0]]
    for curr in intervals[1:]:
      prev = res[-1]
      if curr.start <= prev.end:
        prev.end = max(curr.end, prev.end)
      else:
        res.append(curr)
    return res

def arr_to_interval_list(arr):
  return [Interval(a,b) for (a,b) in arr]

def intervals_to_arr(intervals):
  return [[i.start, i.end] for i in intervals]

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    intervals = arr_to_interval_list([[1,3],[2,6],[8,10],[15,18]])
    self.assertEqual(intervals_to_arr(self.s.merge(intervals)), [[1,6],[8,10],[15,18]])

    intervals = arr_to_interval_list([[0, 5],[15, 20],[5, 10]])
    self.assertEqual(intervals_to_arr(self.s.merge(intervals)), [[0,10], [15,20]])

    intervals = arr_to_interval_list([[1,4],[2,3]])
    self.assertEqual(intervals_to_arr(self.s.merge(intervals)), [[1,4]])



if __name__ == "__main__":
  unittest.main()
