import unittest

# beats 47.67%
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.cache = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.cache) >= self.size:
            self.cache.pop(0)
        self.cache.append(val)
        return sum(self.cache) / float(len(self.cache))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
