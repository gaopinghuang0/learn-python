import unittest

# iteration, 68.87%
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # idea: divide and conquer
        # start from the bottom left, if the value is larger, search the right part
        # if the value is smaller, search the upper part
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


# recursion, beats 28.80%
class SolutionRecursion(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # idea: divide and conquer
        # start from the bottom left, if the value is larger, search the right part
        # if the value is smaller, search the upper part
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        return self.find(m-1, 0, matrix, target, m, n)

    def find(self, i, j, matrix, target, m, n):
        if i < 0 or j >= n:
            return False
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            return self.find(i-1, j, matrix, target, m, n)
        else:
            return self.find(i, j+1, matrix, target, m, n)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    target = 5
    self.assertEqual(self.s.searchMatrix(matrix, target), True)
    target = 20
    self.assertEqual(self.s.searchMatrix(matrix, target), False)

if __name__ == "__main__":
  unittest.main()
