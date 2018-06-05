import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# beats 41.17%
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # idea: two pointers, distance is k, move from left to right
        # linked list may be longer than k or shorter than k
        if not head:
            return head
        left, right = head, head
        node = head
        i = 0
        while node and i < k:
            node = node.next
            i += 1
        if i < k:  # k is larger than len
            size = i
            k = k % size
            node = head
            i = 0
            while i < k:
                node = node.next
                i += 1
            right = node
        else:  # k is shorter than len
            right = node
        if not right:
            return head
        # move two pointers together till the end
        while right.next:
            right = right.next
            left = left.next
        # rotate
        right.next = head
        new_head = left.next
        left.next = None
        return new_head

        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
