import unittest

# beats 99.57%
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}  # msg: timestamp

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.cache:
            ts = self.cache[message]
            if timestamp < ts + 10:
                return False
        self.cache[message] = timestamp
        return True


class TestSolution(unittest.TestCase):
    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        obj = Logger()
        self.assertEqual(obj.shouldPrintMessage(1, 'foo'), True)
        self.assertEqual(obj.shouldPrintMessage(2, 'bar'), True)
        self.assertEqual(obj.shouldPrintMessage(3, 'foo'), False)
        self.assertEqual(obj.shouldPrintMessage(8, 'bar'), False)
        self.assertEqual(obj.shouldPrintMessage(10, 'foo'), False)
        self.assertEqual(obj.shouldPrintMessage(11, 'foo'), True)


if __name__ == "__main__":
    unittest.main()
