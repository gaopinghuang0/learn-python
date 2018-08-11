import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# beats 43.78%
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # idea: reverse, add, reverse again
        dummy = tail = self.reverse(head)
        c = 1
        while c > 0 and tail:
            val = tail.val + c
            c = val // 10
            tail.val = val % 10
            tail = tail.next

        if c > 0:
            new_head = ListNode(1)
            new_head.next = self.reverse(dummy)
            return new_head

        return self.reverse(dummy)

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
