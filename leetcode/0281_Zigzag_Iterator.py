import unittest

# beats 87.90%
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.cache = []
        if v1:
            self.cache.append([0, v1])
        if v2:
            self.cache.append([0, v2])
        self.curr = 0

    def next(self):
        """
        :rtype: int
        """
        idx, arr = self.cache[self.curr]
        # pick the element
        res = arr[idx]
        next_idx = idx + 1
        if next_idx >= len(arr):
            self.cache.pop(self.curr)
            if self.cache:
                self.curr = self.curr % len(self.cache)
        else:
            self.cache[self.curr][0] = next_idx
            self.curr = (self.curr + 1) % len(self.cache)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.cache) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


class TestSolution(unittest.TestCase):
    def setUp(self):
        pass

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        v1 = [1,2]
        v2 = [3,4,5,6]
        i, v = ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        self.assertEqual(v, [1,3,2,4,5,6])
        v1 = [1,2]
        v2 = [3]
        i, v = ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        self.assertEqual(v, [1,3,2])

if __name__ == "__main__":
    unittest.main()
