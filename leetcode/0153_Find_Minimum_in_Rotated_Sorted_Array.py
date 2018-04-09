import unittest

# beats 93.74%
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] < nums[hi]:  # sorted
                return nums[lo]

            mid = (lo + hi) // 2

            if nums[mid] >= nums[lo]:
                # left is sorted
                lo = mid + 1
            else:
                # right is sorted
                hi = mid
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
