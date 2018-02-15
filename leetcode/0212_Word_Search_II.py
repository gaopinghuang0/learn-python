import unittest

# idea from Discuss, beats 52.54%
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # idea: Trie
        # if some words share the same prefix, dfs does not need
        # to start over from the beginning
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, '', res)
        return list(set(res))

    def dfs(self, board, i, j, trie, path, res):
        if '#' in trie:
            res.append(path)   # do not return here, keep dfs
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
            return
        tmp = board[i][j]
        board[i][j] = '*'  # mark as visited
        for direction in [(0,-1),(0,1), (1,0), (-1,0)]:
            x, y = i + direction[0], j + direction[1]
            self.dfs(board, x, y, trie[tmp], path+tmp, res)
        board[i][j] = tmp  # restore

# time limit exceeded
class SolutionTooSlow(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # idea: save the starting pos for each char
        if not board or not board[0] or not words:
            return []
        words = [w for w in words if w]
        char_pos_dict = {}
        for w in words:
            char = w[0]
            if char not in char_pos_dict:
                char_pos_dict[char] = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in char_pos_dict:
                    char_pos_dict[char].append((i,j))
        # print(char_pos_dict)
        res = set()
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for w in words:
            char = w[0]
            if not char_pos_dict[char]:
                continue
            for pos in char_pos_dict[char]:
                if self.dfs_check(pos, board, w, m, n):
                    res.add(w)
                    break
        return list(res)

    def dfs_check(self, pos, board, word, m, n):
        i, j = pos
        temp = board[i][j]
        if temp == word[0] and len(word) == 1:
            return True
        elif temp == word[0] and len(word) > 1:
            board[i][j] = '*'  # mark as visited
            for direction in self.directions:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x < m and 0 <= y < n and board[x][y] != '*':
                    if self.dfs_check((x,y), board, word[1:], m, n):
                        board[i][j] = temp  # restore
                        return True
            board[i][j] = temp  # restore
        return False


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    # self.assertEqual(self.s.findWords(board, words), ['oath', 'eat'])
    board = [["a"]]
    words = ["a"]
    self.assertEqual(self.s.findWords(board, words), ['a'])
    board = [["a"]]
    words = ["a", 'a']
    self.assertEqual(self.s.findWords(board, words), ['a'])

if __name__ == "__main__":
  unittest.main()
