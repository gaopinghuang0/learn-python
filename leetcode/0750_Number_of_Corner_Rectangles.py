import unittest


# idea from Discuss, beats 36.03%
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # idea: fix two rows, check all valid columns, then pick any 2 of those columns
        # namely combination(valid_col, 2)
        # credit: https://leetcode.com/problems/number-of-corner-rectangles/discuss/110196/short-JAVA-AC-solution-(O(m2-*-n))-with-explanation.
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(0, m-1):
            for j in range(i+1, m):
                valid_col = 0
                for k in range(0, n):
                    if grid[i][k] and grid[j][k]:
                        valid_col += 1
                res += valid_col * (valid_col - 1) / 2;  # select 2 out of valid_col
        return res

# too slow
class Solution_V2(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j]:
                    for ii in range(i+1, m):
                        if grid[ii][j]:
                            for jj in range(j+1, n):
                                count += grid[ii][jj] * grid[i][jj]
        return count

# too slow
class Solution_V1(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # idea: recursion
        if not grid or not grid[0] or len(grid) == 1 or len(grid[0]) == 1:
            return 0

        m, n = len(grid), len(grid[0])

        def countGrid(grid, x, y):
            if x > m-2 or y > n-2:  # h or w of rect should be at least 2
                return 0
            count = 0
            for i in range(x, m-1):  # x can be at most m-2
                count += self.countThisCorner(grid, i, y)
            for j in range(y+1, n-1):  # y can be at most n-2
                count += self.countThisCorner(grid, x, j)
            count += countGrid(grid, x+1, y+1)
            return count

        return countGrid(grid, 0, 0)

    def countThisCorner(self, grid, x, y):
        # count the number of grid that uses the corner (x,y) as the top-left corner
        if grid[x][y] == 0:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for dx in range(1, m-x):
            if grid[x+dx][y]:
                for dy in range(1, n-y):
                    if grid[x][y+dy] and grid[x+dx][y+dy]:
                        count += 1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        grid = [[1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1]]
        self.assertEqual(self.s.countCornerRectangles(grid), 1)
        grid = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
        self.assertEqual(self.s.countCornerRectangles(grid), 9)
        grid = [[1, 1, 1, 1]]
        self.assertEqual(self.s.countCornerRectangles(grid), 0)

if __name__ == "__main__":
    unittest.main()
