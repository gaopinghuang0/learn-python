import unittest

# beats 97.79%
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # idea: compare the total kinds with half of total candies
        half_total = len(candies) // 2
        total_kinds = len(set(candies))
        return half_total if half_total <= total_kinds else total_kinds


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.distributeCandies([1,1,2,2,3,3]), 3)
        self.assertEqual(self.s.distributeCandies([1,1,2,3]), 2)


if __name__ == "__main__":
    unittest.main()
