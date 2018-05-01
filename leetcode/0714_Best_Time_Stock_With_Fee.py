
# beats 94.85%
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # idea: only start a new transaction if the old_high - new_low > fee
        # namely, keep the same transaction when the new low stock is not low enough
        if len(prices) < 2:
            return 0
        res = 0
        low, high = prices[0], prices[0]
        for p in prices[1:]:
            if p >= high:
                high = p
            elif high - p > fee: # starts a new transaction
                res += max(high-low-fee, 0)
                low, high = p, p
            else:
                if p < low:
                    low, high = p, p
        res += max(high-low-fee, 0)
        return res

sol = Solution()
print(sol.maxProfit([1,3,2,8,4,9], 2))  # 8
print(sol.maxProfit([1,4,2,8,4,9], 2))  # 8
print(sol.maxProfit([1,5,2,8,4,9], 2))  # 9
print(sol.maxProfit([2,1,4,4,2,3,2,5,1,2], 1))  #4