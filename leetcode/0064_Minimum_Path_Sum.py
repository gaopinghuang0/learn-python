import unittest

# O(n2) space
class Solution0(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in xrange(n)] for y in xrange(m)]
        # for j, x in enumerate(grid[0]):
        #     dp[0][j] = dp[0][j-1] + x
        # for i in xrange(m):
        #     dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in xrange(m):
            for j in xrange(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
                # print i, j, dp
        return dp[m-1][n-1]

 # O(n) space
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [grid[0][0]]   # dp[i] means the i-th column
        for i in xrange(1, n):
            dp.append(dp[-1] + grid[0][i])
        for i in xrange(1, m):
            pre = dp[0] + grid[i][0]
            for j in xrange(1, n):
                dp[j] = min(dp[j], pre) + grid[i][j]
                pre = dp[j]
            dp[0] += grid[i][0]
        return dp[-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        grid = [[3, 2, 4], [5, 6, 7], [4, 1, 8], [7, 8, 10]]
        self.assertEqual(self.s.minPathSum(grid), 30)
        grid = [[1]]
        self.assertEqual(self.s.minPathSum(grid), 1)


if __name__ == "__main__":
    unittest.main()
