import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# beats 50.15%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # idea: two pointers, one moves one step at a time, another moves two steps at a time
        if not head or not head.next:
            return False
        p1 = head.next
        p2 = head.next.next
        while p1 and p2 and p2.next:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
