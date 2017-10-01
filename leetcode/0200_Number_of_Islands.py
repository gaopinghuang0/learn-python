import unittest


class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def sink(i, j):
      if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        grid[i][j] = '0'
        map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
        return 1
      return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  unittest.main()
