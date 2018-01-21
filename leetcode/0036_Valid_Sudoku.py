import unittest

from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        row_vals = defaultdict(set)
        col_vals = defaultdict(set)
        sub_vals = defaultdict(set)

        for row in range(m):
            for col in range(n):
                c = board[row][col]
                if c == '.':
                    continue
                sub = str(row / 3) + str(col / 3)
                if c in row_vals[row] or c in col_vals[col] or c in sub_vals[sub]:
                    return False

                row_vals[row].add(c)
                col_vals[col].add(c)
                sub_vals[sub].add(c)
        return True
# slow
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        # check each row
        for i in range(m):
            row = [x for x in board[i] if x != '.']
            if len(row) != len(set(row)):
                return False
        # check each column
        for j in range(n):
            col = [board[i][j] for i in range(m) if board[i][j] != '.']
            if len(col) != len(set(col)):
                return False
        # check 9 sub-board
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                sub = [board[ii][jj] for ii in range(i,i+3) for jj in range(j,j+3) if board[ii][jj] != '.']
                if len(sub) != len(set(sub)):
                    return False
        return True

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
