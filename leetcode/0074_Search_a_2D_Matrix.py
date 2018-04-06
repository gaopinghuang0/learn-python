import unittest

# beats 97.47%
from bisect import bisect_left
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # idea: divide and conquer, first compare the target with the bottom-left corner
        # if it's smaller, search the above part, if larger, search the current row
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        down = m-1
        while down >= 0:
            pivot = matrix[down][0]  # the bottom-left corner
            if target == pivot:
                return True
            elif target > pivot:
                idx = bisect_left(matrix[down], target)
                if idx < n and matrix[down][idx] == target:
                    return True
                return False
            else:
                down -= 1
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        self.assertEqual(self.s.searchMatrix(matrix, 3), True)
        self.assertEqual(self.s.searchMatrix(matrix, 16), True)
        self.assertEqual(self.s.searchMatrix(matrix, 21), False)


if __name__ == "__main__":
    unittest.main()
