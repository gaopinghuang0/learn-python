import unittest

# beats no data
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # idea: binary search
        lo, hi = 0, len(A)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] < A[mid+1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.peakIndexInMountainArray([0,1,0]), 1)
        self.assertEqual(self.s.peakIndexInMountainArray([0,2,1,0]), 1)


if __name__ == "__main__":
    unittest.main()
