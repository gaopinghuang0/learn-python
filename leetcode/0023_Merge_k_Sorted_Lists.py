import unittest

from utils.ListHelper import array_to_list, linked_list_to_array

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import *
class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    root = node = ListNode(None)
    hp = []
    for _list in lists:
      if _list:
        heappush(hp, (_list.val, _list))
    while hp:
      val, curr_node = heappop(hp)
      node.next = curr_node
      if curr_node.next:
        next_node = curr_node.next
        heappush(hp, (next_node.val, next_node))
      node = node.next
    return root.next


      


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    lists = [array_to_list([1,2,4]), array_to_list([3,5,6]), array_to_list([7,8])]
    self.assertEqual(linked_list_to_array(self.s.mergeKLists(lists)), list(range(1,9)))
    lists = []
    self.assertEqual(linked_list_to_array(self.s.mergeKLists(lists)), [])
    lists = [[]]
    self.assertEqual(linked_list_to_array(self.s.mergeKLists(lists)), [])


if __name__ == "__main__":
  unittest.main()
