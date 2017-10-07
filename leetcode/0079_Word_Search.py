import unittest


class Solution(object):
  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not board:
      return False
    if not self.preCheck(board, word):
      return False
    for i in range(len(board)):
      for j in range(len(board[0])):
        if self.dfs(board, i, j, word):
          return True
    return False

  def preCheck(self, board, word):
    from collections import Counter
    counter = Counter(word)

    for i in board:
      for j in i:
        if j in counter:
          counter[j] -= 1
    if counter.most_common(1)[1] > 0:
      return False
    return True

  def dfs(self, board, i, j, word):
    if not word:
      return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
      return False

    tmp = board[i][j]  # cache
    if tmp != word[0]:
      return False
    board[i][j] = '#'  # avoid visiting again
    ans = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or\
      self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])

    board[i][j] = tmp  # reset
    return ans

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
