import unittest

# beats 94.60%
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return True

        m, n = len(matrix), len(matrix[0])
        def check_diagonal(x, y):
            num = matrix[x][y]
            x += 1
            y += 1
            while x < m and y < n:
                if matrix[x][y] != num:
                    return False
                x += 1
                y += 1
            return True

        for x in range(m):
            if not check_diagonal(x, 0):
                return False

        for y in range(1, n):
            if not check_diagonal(0, y):
                return False
        return True



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        matrix = [
          [1,2,3,4],
          [5,1,2,3],
          [9,5,1,2]
        ]
        self.assertEqual(self.s.isToeplitzMatrix(matrix), True)
        matrix = [
          [1,2],
          [2,2]
        ]
        self.assertEqual(self.s.isToeplitzMatrix(matrix), False)


if __name__ == "__main__":
    unittest.main()
