import unittest


# beats 60.19%
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # idea: DFS, adapted from Discussion
        # use two matrice to store if each ocean can reach a point
        # finally, if a point can be reached from two oceans, that is what we need
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        p_visited = [[0]*n for _ in range(m)]
        a_visited = [[0]*n for _ in range(m)]
        self.directions = [[-1,0], [1,0], [0,-1], [0,1]]

        for i in range(m):
            # left edge and right edge
            self.dfs(i, 0, matrix, p_visited, m, n)
            self.dfs(i, n-1, matrix, a_visited, m, n)
        for j in range(n):
            # top edge and bottom edge
            self.dfs(0, j, matrix, p_visited, m, n)
            self.dfs(m-1, j, matrix, a_visited, m, n)
        # detect the overlapping of two oceans
        ans = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i,j])
        return ans

    def dfs(self, i, j, matrix, visited, m, n):
        # when dfs is called, the index is guaranteed to be valid
        visited[i][j] = True
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(x, y, matrix, visited, m, n)

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
