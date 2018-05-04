import unittest

# idea from Discuss, beats 35.01%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # idea from Discuss: finite state machine
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/126065/Two-DP-methods-using-graph-for-easy-to-understand-with-detail-explanation
        # rest[i] = max(sold[i-1], rest[i-1])
        # hold[i] = max(rest[i-1]-price[i], hold[i-1])
        # sold[i] = hold[i-1] + price[i]
        sold, rest = 0, 0
        hold = float('-inf')
        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)
        return max(rest, sold)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.maxProfit([1,2,3,0,2]), 3)
        self.assertEqual(self.s.maxProfit([1,4,3,8]), 7)


if __name__ == "__main__":
    unittest.main()
