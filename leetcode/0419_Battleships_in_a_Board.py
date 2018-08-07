import unittest

# beats 25.37%
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # idea: dfs and modify board
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = '.'
            for x,y in [(-1,0), (1,0), (0,1), (0,-1)]:
                ii, jj = x+i, y+j
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'X':
                    dfs(ii, jj)

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    dfs(i, j)
                    count += 1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
        self.assertEqual(self.s.countBattleships(board), 2)


if __name__ == "__main__":
    unittest.main()
