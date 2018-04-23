import unittest

# beats 94.68%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # idea: one pass from left to right
        if not prices:
            return 0
        left, right = prices[0], prices[0]
        res = 0
        for p in prices:
            if p >= right:
                right = p
            else:
                res += right-left
                left, right = p, p
        res += right - left
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.maxProfit([7,1,5,3,6,4]), 7)
        self.assertEqual(self.s.maxProfit([1,2,3,4,5]), 4)
        self.assertEqual(self.s.maxProfit([7,6,4,3,1]), 0)


if __name__ == "__main__":
    unittest.main()
