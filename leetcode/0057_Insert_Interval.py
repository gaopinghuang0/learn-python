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
    ans = []
    if not intervals:
      return [newInterval]
    if not newInterval:
      return intervals

    # handle two sides
    start = newInterval.start
    end = newInterval.end
    if end < intervals[0].start:
      return [newInterval]+intervals
    elif start > intervals[-1].end:
      return intervals + [newInterval]

    for i, intv in enumerate(intervals):
      if newInterval.start <= intv.end:
        start = min(intv.start, start)
        
        is_jump = False
        for j, _intv in enumerate(intervals[i:], i):
          if newInterval.end >= _intv.start:
            end = max(newInterval.end, _intv.end)
          else:
            is_jump = True
            break
        ans.append(Interval(start, end))
        if is_jump:
            ans += intervals[j:]
        break
      else:
        ans.append(intv)

    return ans



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
