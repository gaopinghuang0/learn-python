import unittest

# beats 14.51%
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # idea: use a stack
        x, y = click
        if board[x][y] == 'M':  # click on the mine
            board[x][y] = 'X'
            return board

        stack = set([(x,y)])
        m, n = len(board), len(board[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
        while stack:
            x,y = stack.pop()
            # check number of mines in adjacent cells
            count = 0
            next_cell = set()
            for dx, dy in direction:
                i = x + dx
                j = y + dy
                if 0 <= i < m and 0 <= j < n:
                    val = board[i][j]
                    if val == 'M':
                        count += 1
                    elif val == 'E':
                        next_cell.add((i,j))
                    else:  # 'B' or 'digit'
                        pass
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                stack = stack.union(next_cell)
        return board

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
        click = [3,0]
        output = [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'M', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]
        self.assertEqual(self.s.updateBoard(board, click), output)
        board = [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'M', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]
        click = [1,2]
        output = [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'X', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]
        self.assertEqual(self.s.updateBoard(board, click), output)


if __name__ == "__main__":
    unittest.main()
