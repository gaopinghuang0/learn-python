import unittest

from utils.ListHelper import array_to_list, linked_list_to_array

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = n = ListNode(None)
    while l1 and l2:
      if l1.val >= l2.val:
        n.next = l2
        n = n.next
        l2 = l2.next
      else:
        n.next = l1
        n = n.next
        l1 = l1.next
    if not l1:
      n.next = l2
    else:
      n.next = l1

    return head.next



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    l1 = array_to_list([1,2,3])
    l2 = array_to_list([1,2,3])
    res = linked_list_to_array(self.s.mergeTwoLists(l1, l2))
    self.assertEqual(res, [1,1,2,2,3,3])

    l1 = array_to_list([2,2,3])
    l2 = array_to_list([1,2,3])
    res = linked_list_to_array(self.s.mergeTwoLists(l1, l2))
    self.assertEqual(res, [1,2,2,2,3,3])

    l1 = array_to_list([])
    l2 = array_to_list([1,2,3])
    res = linked_list_to_array(self.s.mergeTwoLists(l1, l2))
    self.assertEqual(res, [1,2,3])

    l1 = array_to_list([])
    l2 = array_to_list([])
    res = linked_list_to_array(self.s.mergeTwoLists(l1, l2))
    self.assertEqual(res, [])

    l1 = array_to_list([-4, -3, 2, 6, 8])
    l2 = array_to_list([1,2,3])
    res = linked_list_to_array(self.s.mergeTwoLists(l1, l2))
    self.assertEqual(res, [-4, -3, 1, 2, 2, 3, 6, 8])



if __name__ == "__main__":
  unittest.main()
