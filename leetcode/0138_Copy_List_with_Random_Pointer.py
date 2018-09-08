import unittest


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


# beats 99.18%
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # idea 1: use a dict to store the {oldNode: newNode}
        if not head:
            return None
        cache = {None: None}
        node = head
        while node:
            newNode = RandomListNode(node.label)
            cache[node] = newNode
            node = node.next
        # now deal with the next and random link
        node = head
        while node:
            newNode = cache[node]
            newNode.next = cache[node.next]
            newNode.random = cache[node.random]
            node = node.next
        return cache[head]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
