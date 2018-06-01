import unittest

# idea from Discuss, beats 83.48%
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39615/My-explanation-for-O(N)-solution!
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # idea from Discuss, DP or Finite State Machine
        # use four variables, buy1, sell1, buy2, sell2
        # or equivalently, buy1[i], sell1[i], buy2[i], sell2[i]
        # 
        # sell2: Final profit.
        # buy2: Best profit so far, if you buy the stock not after Day i (2nd transaction).
        # sell1: Best profit so far, if you sell the stock not after Day i (1st transaction).
        # buy1: Minimum price to buy the stock.
        buy1 = -float("inf")
        buy2 = -float("inf")
        sell1, sell2 = 0, 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)  # because buy1 is negative
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2

from heapq import heappush, heappop
class Solution_wrong(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # idea: two pointers and a max-heap, left to right, lo and hi, min_lo and max_hi
        # two cases:
        # 1. if not met a lower price, keep lo, update hi, store each increasing segment 
        # and store the sum of two largest segment
        # 2. if met a lower price, update lo, use (lo,hi) to represent a single segment and repeat
        if not prices:
            return 0
        global_hp = []
        temp_hp = []  # update whenever met a smaller min_lo
        left, right = prices[0], prices[0]
        min_lo = left
        max_hi = right
        res = 0
        for p in prices[1:]+[-float('inf')]:
            if p >= right:  # increasing
                if p > max_hi:
                    max_hi = p
            else:  # decreasing or equal
                # push a new segment
                heappush(temp_hp, left-right)
                left = p
                # print(temp_hp)
                # get the sum of largest two segments
                if len(temp_hp) >= 2:
                    x = heappop(temp_hp)
                    y = heappop(temp_hp)
                    temp_sum = -(x+y)
                    if res < temp_sum:
                        res = temp_sum
                    heappush(temp_hp, x)
                    heappush(temp_hp, y)
                # only keep the largest segment
                heappush(temp_hp, min_lo-max_hi)
                temp_hp = [heappop(temp_hp)]
                # print(temp_hp)
                if p < min_lo:
                    min_lo = p
                    max_hi = p
                    heappush(global_hp, temp_hp[0])
                    temp_hp = []
            right = p
            # print(p,temp_hp, global_hp, min_lo, max_hi, res)
        # get the sum of largest two segments
        if len(global_hp) >= 2:
            x = heappop(global_hp)
            y = heappop(global_hp)
            temp_sum = -(x+y)
            if res < temp_sum:
                res = temp_sum
            heappush(global_hp, x)
            heappush(global_hp, y)
        elif len(global_hp) == 1:
            if res < -global_hp[0]:
                res = -global_hp[0]
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.maxProfit([3,3,5,0,0,3,1,4]), 6)
        self.assertEqual(self.s.maxProfit([1,3,2,5,0,0,3,1,4]), 8)
        self.assertEqual(self.s.maxProfit([1,3,2,7,2,5,0,0,3,1,4]), 10)
        self.assertEqual(self.s.maxProfit([1,2,3,4,5]), 4)
        self.assertEqual(self.s.maxProfit([7,6,4,3,1]), 0)
        # (1,7) and (2, 9)
        self.assertEqual(self.s.maxProfit([1,2,4,2,5,7,2,4,9,0]), 13)
        # (2,8) and (0,9)
        self.assertEqual(self.s.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]), 15)
        # (4,8) and (6,9)
        self.assertEqual(self.s.maxProfit([6,5,4,8,6,8,7,8,9,4,5]), 7)


if __name__ == "__main__":
    unittest.main()
