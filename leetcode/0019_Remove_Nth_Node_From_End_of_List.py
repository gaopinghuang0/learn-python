import unittest

from utils.ListHelper import array_to_list, linked_list_to_array

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    node1 = node2 = head
    # find the Nth node from start
    while n > 0:
      node2 = node2.next
      n -= 1
    if not node2:
      return head.next      
    # move the node to the end
    while node2.next:
      node1 = node1.next
      node2 = node2.next
    node1.next = node1.next.next
    return head



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    head = array_to_list([1])
    n = 1
    res = linked_list_to_array(self.s.removeNthFromEnd(head, n))
    self.assertEqual(res, [])

    head = array_to_list([1, 2])
    n = 2
    res = linked_list_to_array(self.s.removeNthFromEnd(head, n))
    self.assertEqual(res, [2])

    head = array_to_list([1, 2, 3, 4, 5])
    n = 2
    res = linked_list_to_array(self.s.removeNthFromEnd(head, n))
    self.assertEqual(res, [1, 2, 3, 5])

    head = array_to_list([1, 2, 3, 4, 5, 6, 7])
    n = 5
    res = linked_list_to_array(self.s.removeNthFromEnd(head, n))
    self.assertEqual(res, [1, 2, 4, 5, 6, 7])

if __name__ == "__main__":
  unittest.main()
