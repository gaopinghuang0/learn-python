import unittest

# idea from Discuss, beats 85.11%
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea from Discuss: O(n) time and O(1) space
        # http://keithschwarz.com/interesting/code/?dir=find-duplicate
        # the nums[0] must be outside of the cycle since other num
        # is range from 1 to n and cannot reach 0
        slow = 0
        fast = 0

        # they will meet inside the cycle (loop)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find the entry of the cycle
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            # if the two hit, the intersection is the duplicate element
            if slow == finder:
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
