import unittest

# beats 88.12%
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # idea: DP, similar to 0123_Best_Time_to_Buy_and_Sell_Stock_III.py
        n = len(prices)
        if n < 2:
            return 0
        # k is big enougth to cover all ramps.
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) \
                       if i - j > 0)
        buy = [float('-inf')] * (k+1)
        sell = [0] * (k+1)
        for price in prices:
            for i in range(1, k+1):
                temp = sell[i-1] - price
                if buy[i] < temp:
                    buy[i] = temp
                temp = buy[i] + price
                if sell[i] < temp:
                    sell[i] = temp
        return sell[k]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.maxProfit(1, [2,4,1]), 2)
        self.assertEqual(self.s.maxProfit(2, [2,4,1]), 2)
        self.assertEqual(self.s.maxProfit(2, [3,2,6,5,0,3]), 7)
        self.assertEqual(self.s.maxProfit(2, [3,3,5,0,0,3,1,4]), 6)
        self.assertEqual(self.s.maxProfit(2, [1,3,2,5,0,0,3,1,4]), 8)
        self.assertEqual(self.s.maxProfit(2, [1,3,2,7,2,5,0,0,3,1,4]), 10)
        self.assertEqual(self.s.maxProfit(2, [1,2,3,4,5]), 4)
        self.assertEqual(self.s.maxProfit(2, [7,6,4,3,1]), 0)
        # (1,7) and (2, 9)
        self.assertEqual(self.s.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]), 13)
        # (2,8) and (0,9)
        self.assertEqual(self.s.maxProfit(2, [8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]), 15)
        # (4,8) and (6,9)
        self.assertEqual(self.s.maxProfit(2, [6,5,4,8,6,8,7,8,9,4,5]), 7)
        self.assertEqual(self.s.maxProfit(3, [3,2,6,5,0,3]), 7)
        self.assertEqual(self.s.maxProfit(3, [6,5,4,8,6,8,7,8,9,4,5]), 8)


if __name__ == "__main__":
    unittest.main()
