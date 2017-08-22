import unittest

from utils.ListHelper import ListNode, array_to_list, print_linked_list, linked_list_to_array

# other's solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        carry = 0
        root = n = ListNode(0)
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val = v1 + v2 + carry
            if val >= 10:
                val = (v1 + v2 + carry) - 10
                carry = 1
            else:
                carry = 0

            n.next = ListNode(val)
            n = n.next

        return root.next


# My own solution
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         res = []
#         carry = 0

#         while l1 and l2:
#             x = l1.val + l2.val + carry
#             if x >= 10:
#                 carry = 1
#                 res.append(x-10)
#             else:
#                 carry = 0
#                 res.append(x)
#             l1 = l1.next
#             l2 = l2.next

#         if l2 and not l1:
#             while l2:
#                 x = l2.val + carry
#                 if x >= 10:
#                     carry = 1
#                     res.append(x-10)
#                 else:
#                     carry = 0
#                     res.append(x)
#                 l2 = l2.next
#         elif l1 and not l2:
#             while l1:
#                 x = l1.val + carry
#                 if x >= 10:
#                     carry = 1
#                     res.append(x-10)
#                 else:
#                     carry = 0
#                     res.append(x)
#                 l1 = l1.next
#         if carry:
#             res.append(carry)

#         return array_to_list(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        list1 = array_to_list([2])
        list2 = array_to_list([5,6,4])
        res = [7,6,4]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)

        list1 = array_to_list([2,4,3])
        list2 = array_to_list([5])
        res = [7,4,3]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)

        list1 = array_to_list([0])
        list2 = array_to_list([5])
        res = [5]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)

        # special case
        list1 = array_to_list([5])
        list2 = array_to_list([5])
        res = [0, 1]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)
        list1 = array_to_list([1, 6])
        list2 = array_to_list([1, 5])
        res = [2, 1, 1]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)

        # special case
        list1 = array_to_list([1, 9, 9])
        list2 = array_to_list([9])
        res = [0, 0, 0, 1]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)

        list1 = array_to_list([2,4,3])
        list2 = array_to_list([5,6,4])
        res = [7,0,8]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)

        list1 = array_to_list([2,4,3,6])
        list2 = array_to_list([5,6,4])
        res = [7,0,8,6]
        self.assertEqual(linked_list_to_array(self.s.addTwoNumbers(list1, list2)), res)


if __name__ == "__main__":
    unittest.main()
