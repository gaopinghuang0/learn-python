import unittest

# beats 18.13%
# but the idea happen to be the same as the fastest submission
# I guess it adds more test cases after that submission
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # idea: get all the rows and columns that contain 0, set to 0 later
        if not matrix or not matrix[0]:
            return
        rows = set()
        cols = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        matrix = [[1,2,3],[4,0,6],[7,8,9]]
        self.s.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,3],[0,0,0],[7,0,9]])


if __name__ == "__main__":
    unittest.main()
