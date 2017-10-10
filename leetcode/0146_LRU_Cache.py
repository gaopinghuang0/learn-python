import unittest


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.cache = []   # store the keys, the rightmost is the least recent used key
        self.d = {}   # {key: value}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
          # update cache
          if self.cache[0] != key:
            self.cache.remove(key)
            self.cache.insert(0, key)
          return self.d[key]
        else:
          return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
          if self.cache[0] != key:
            self.cache.remove(key)
            self.cache.insert(0, key)
          self.d[key] = value
        elif len(self.cache) == self.c:
          # evict and insert
          old_key = self.cache.pop()
          del self.d[old_key]
          self.d[key] = value
          self.cache.insert(0, key)
        else:
          # insert
          self.d[key] = value
          self.cache.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
