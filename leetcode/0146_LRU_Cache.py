import unittest


# Credit: adapted from https://discuss.leetcode.com/topic/34701/java-easy-version-to-understand
# idea, dict + doubly-linked list, O(1) time
class Node(object):
  def __init__(self, key, value):
    self.key = key
    self.val = value
    self.prev = None
    self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

        self.d = {}   # {key: Node}

    def delete_node(self, node):
      node.prev.next = node.next
      node.next.prev = node.prev

    def add_to_head(self, node):
      node.next = self.head.next
      self.head.next = node
      node.next.prev = node
      node.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
          # update cache
          node = self.d[key]
          self.delete_node(node)
          self.add_to_head(node)
          return node.val
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
          node = self.d[key]
          self.delete_node(node)
          self.add_to_head(node)
          node.val = value
        else:
          node = Node(key, value)
          if len(self.d) >= self.c:
            # evict and insert
            old_node = self.tail.prev
            del self.d[old_node.key]
            self.delete_node(old_node)
            self.d[key] = node
            self.add_to_head(node)
          else:
            # insert
            self.d[key] = node
            self.add_to_head(node)


# idea: dict + list, O(n) time
# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.c = capacity
#         self.cache = []   # store the keys, the rightmost is the least recent used key
#         self.d = {}   # {key: value}

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key in self.d:
#           # update cache
#           if self.cache[0] != key:
#             self.cache.remove(key)
#             self.cache.insert(0, key)
#           return self.d[key]
#         else:
#           return -1
        

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if key in self.d:
#           if self.cache[0] != key:
#             self.cache.remove(key)
#             self.cache.insert(0, key)
#           self.d[key] = value
#         elif len(self.cache) == self.c:
#           # evict and insert
#           old_key = self.cache.pop()
#           del self.d[old_key]
#           self.d[key] = value
#           self.cache.insert(0, key)
#         else:
#           # insert
#           self.d[key] = value
#           self.cache.insert(0, key)


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
