import unittest


# beats 14.64%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # allow duplicates
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] < nums[hi]:  # sorted
                return nums[lo]

            mid = (lo + hi) // 2

            if nums[mid] > nums[lo]:
                # left is sorted and min must be on the right
                lo = mid + 1
            elif nums[mid] < nums[lo]:
                # right is sorted and min must be on the left
                hi = mid
            else:
                lo += 1
        return nums[hi]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
