import unittest

import bisect
# beats 100%
class HitCounter(object):
    # idea: use bisect

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.history.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        j = bisect.bisect_right(self.history, timestamp)
        i = bisect.bisect_right(self.history, timestamp-300)
        return j - i


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = HitCounter()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.s.hit(1)
        self.s.hit(2)
        self.s.hit(3)
        self.assertEqual(self.s.getHits(4), 3)
        self.s.hit(300)
        self.assertEqual(self.s.getHits(300), 4)
        self.assertEqual(self.s.getHits(301), 3)


if __name__ == "__main__":
    unittest.main()
