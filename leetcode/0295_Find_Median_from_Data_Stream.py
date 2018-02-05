import unittest

# beats 98.93%
from heapq import heappush, heappop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # idea: use two heap
        self.median = 0
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if num >= self.median:
            # add to large
            heappush(self.large, num)
            if len(self.large) == len(self.small) + 2:
                temp = heappop(self.large)
                heappush(self.small, -temp)
                self.median = (temp + self.large[0]) / 2.0
            elif len(self.large) == len(self.small) + 1:
                self.median = self.large[0]
            else:
                self.median = (-self.small[0] + self.large[0]) / 2.0
        else:
            # add to small
            heappush(self.small, -num)
            if len(self.small) == len(self.large) + 2:
                temp = -heappop(self.small)
                heappush(self.large, temp)
                self.median = (temp - self.small[0]) / 2.0
            elif len(self.small) == len(self.large) + 1:
                self.median = -self.small[0]
            else:
                self.median = (-self.small[0] + self.large[0]) / 2.0
        # print(self.small, self.large, self.median)

    def findMedian(self):
        """
        :rtype: float
        """
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = MedianFinder()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    self.s.addNum(6)
    print(self.s.findMedian())
    self.s.addNum(10)
    print(self.s.findMedian())
    self.s.addNum(2)
    print(self.s.findMedian())
    self.s.addNum(6)
    print(self.s.findMedian())


if __name__ == "__main__":
  unittest.main()
