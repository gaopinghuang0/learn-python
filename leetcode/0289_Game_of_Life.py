import unittest

# beats 41.91%
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # requirement: update in-place at the same time
        # idea: use encoding rule to save old and new value at the same time
        # 020 (dead-to-dead), 021 (dead-to-live), 120 (live-to-dead), 121 (live-to-live)
        # namely 4 (dead-dead), 5 (dead-live), 6 (live-dead), 7 (live-live)
        # in the end, update each value to 0 or 1
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        self.m = m
        self.n = n
        self.board = board
        for i in range(m):
            for j in range(n):
                count = sum(map(self.is_live, [(i-1, j), (i-1, j-1), (i-1, j+1),
                                (i, j-1), (i, j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]))

                live = self.is_live((i,j))
                if live and (count < 2 or count > 3):
                    board[i][j] = 120
                elif live and 2 <= count <= 3:
                    board[i][j] = 121
                elif not live and count == 3:
                    board[i][j] = 21
        # update
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] % 2

    def is_live(self, pos):
        if 0 <= pos[0] < self.m and 0 <= pos[1] < self.n:
            cell = self.board[pos[0]][pos[1]]
            return 1 if cell in [1, 120, 121] else 0
        return 0

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
