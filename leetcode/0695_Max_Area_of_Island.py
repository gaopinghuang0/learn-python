import unittest

# beats 89.37%
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1)
            return 0
        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
