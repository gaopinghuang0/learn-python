import unittest

# beats 24.85%
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # idea: increase to the min of col-row for i,j
        m, n = len(grid), len(grid[0])
        row = [0]*m
        col = [0]*n
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val > row[i]:
                    row[i] = val
                if val > col[j]:
                    col[j] = val
        res = 0
        for i in range(m):
            for j in range(n):
                res += min(row[i], col[j]) - grid[i][j]
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        grid = [[3,0,8,4],
                [2,4,5,7],
                [9,2,6,3],
                [0,3,1,0]]
        gridNew = [ [8, 4, 8, 7],
                    [7, 4, 7, 7],
                    [9, 4, 8, 7],
                    [3, 3, 3, 3] ]
        self.assertEqual(self.s.maxIncreaseKeepingSkyline(grid), 35)


if __name__ == "__main__":
    unittest.main()
