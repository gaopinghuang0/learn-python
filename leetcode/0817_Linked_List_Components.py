import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# beats 75.92%
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        if not head:
            return 0
        subset = set(G)
        res = 0
        connected = False
        node = head
        while node:
            if node.val in subset:
                connected = True
            elif connected:
                res += 1
                connected = False
            node = node.next
        if connected:
            res += 1
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
