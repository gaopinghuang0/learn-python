import unittest


# done by Discussion, beats 44.63%
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # use cache to save some time
        if not matrix or not matrix[0]:
          return 0
        m, n = len(matrix), len(matrix[0])
        self.directions = [[-1,0], [1,0], [0,-1], [0,1]]
        cache = [[False]*n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                cur_len = self.dfs(i, j, matrix, cache, m, n)
                ans = max(cur_len, ans)
        return ans

    def dfs(self, i, j, matrix, cache, m, n):
        if cache[i][j]:
            return cache[i][j]
        ans = 1
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            cur_len = 1 + self.dfs(x, y, matrix, cache, m, n)
            ans = max(ans, cur_len)
        cache[i][j] = ans
        return ans

# correct but Time Limit Exceeded
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
          return 0
        m, n = len(matrix), len(matrix[0])
        self.directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = [[False]*n for _ in range(m)]
        self.max_len = 1
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, matrix, visited, m, n, 1)
        return self.max_len

    def dfs(self, i, j, matrix, visited, m, n, path_len):
        visited[i][j] = True
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] <= matrix[i][j]:
                continue
            self.max_len = max(path_len+1, self.max_len)
            self.dfs(x, y, matrix, visited, m, n, path_len+1)
        visited[i][j] = False

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    print(self.s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))


if __name__ == "__main__":
  unittest.main()
