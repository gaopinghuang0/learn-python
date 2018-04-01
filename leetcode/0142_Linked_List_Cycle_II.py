import unittest



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# beats 39.39%
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # the same idea as 0287 find duplicate number
        slow = head
        fast = head
        while True:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break
            else:
                return None  # no cycle

        finder = head
        while finder != slow:
            slow = slow.next
            finder = finder.next
        return slow


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
