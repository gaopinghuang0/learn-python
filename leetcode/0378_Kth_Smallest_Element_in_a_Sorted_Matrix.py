import unittest

# beats 26.96%
from heapq import heappush, heappop
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # idea: min-heap
        hp = []
        n = len(matrix)
        visited = [[0]*n for _ in range(n)]
        heappush(hp, (matrix[0][0], 0, 0))
        visited[0][0] = 1
        i = 0
        while True:
            val, x, y = heappop(hp)
            i += 1
            if i == k:
                return val
            # add val's neighbor
            new_x = x + 1
            if new_x < n and not visited[new_x][y]:
                heappush(hp, (matrix[new_x][y], new_x, y))
                visited[new_x][y] = 1
            new_y = y + 1
            if new_y < n and not visited[x][new_y]:
                heappush(hp, (matrix[x][new_y], x, new_y))
                visited[x][new_y] = 1



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        matrix = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ]
        k = 8
        self.assertEqual(self.s.kthSmallest(matrix, k), 13)
        self.assertEqual(self.s.kthSmallest(matrix, 1), 1)
        self.assertEqual(self.s.kthSmallest(matrix, 9), 15)


if __name__ == "__main__":
    unittest.main()
