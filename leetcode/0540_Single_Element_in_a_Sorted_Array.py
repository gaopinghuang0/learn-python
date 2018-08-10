import unittest

# beats 100%
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: binary search
        n = len(nums)  # n must be odd
        lo, hi = 0, n-1
        while lo < hi:  # hi must be >= lo+2
            mid = (lo + hi) // 2  # mid must > lo
            if nums[mid] == nums[mid-1]:
                if (mid - lo + 1) % 2 == 0:
                    lo = mid + 1
                else:
                    hi = mid - 2
            elif nums[mid] == nums[mid+1]:
                if (mid - lo + 1) % 2 == 0:
                    hi = mid - 1
                else:
                    lo = mid + 2
            else:
                return mid

        return nums[hi]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.singleNonDuplicate([1]), 1)
        self.assertEqual(self.s.singleNonDuplicate([1,1,3]), 3)
        self.assertEqual(self.s.singleNonDuplicate([1,3,3]), 1)
        self.assertEqual(self.s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]), 2)
        self.assertEqual(self.s.singleNonDuplicate([3,3,7,7,10,11,11]), 10)


if __name__ == "__main__":
    unittest.main()
