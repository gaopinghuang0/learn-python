import unittest


class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # note: no parentheses
    # Credit: https://discuss.leetcode.com/topic/22948/my-dp-approach-in-python-with-comments-and-unittest/9
    # idea: 2D dp
    # dp[i][j] for s[:i] and p[:j]
    m, n = len(s) + 1, len(p) + 1
    matches = [[False] * n for _ in range(m)]

    # match two empty input
    matches[0][0] = True

    # match empty s with .*
    for i, elem in enumerate(p[1:], 2):
      matches[0][i] = matches[0][i-2] and elem == '*'

    print(matches)
    for i, ss in enumerate(s, 1):
      for j, pp in enumerate(p, 1):
        if pp != '*':
          # update diagonal of dp
          matches[i][j] = matches[i-1][j-1] and (ss == pp or pp == '.')
        else:
          #   p a b *
          # c 1 0 0 0
          # a 0
          # b 0
          # b 0
          # ==>
          #   p a b *
          # c 1 0 0 0
          # a 0 1 0 1
          # b 0 0 1 ?
          # b 0 0 0 ?
          # first ignore the char before *, horizontal update [j-2]
          matches[i][j] |= matches[i][j-2]

          # then consider the char before *, either equal to s[i-1] or be '.'
          # vertical update [i-1]
          if p[j-2] == s[i-1] or p[j-2] == '.':
            matches[i][j] |= matches[i-1][j]

    return matches[-1][-1]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.isMatch('', ''), True)
    self.assertEqual(self.s.isMatch('', 'a*'), True)
    self.assertEqual(self.s.isMatch('aa', 'a'), False)
    self.assertEqual(self.s.isMatch('aa', '.'), False)
    self.assertEqual(self.s.isMatch('aa', '..'), True)
    self.assertEqual(self.s.isMatch('a', '.'), True)
    self.assertEqual(self.s.isMatch('a', ''), False)
    self.assertEqual(self.s.isMatch('aa', 'aa'), True)
    self.assertEqual(self.s.isMatch('aaa', 'aa'), False)
    self.assertEqual(self.s.isMatch('aa', 'a*'), True)
    self.assertEqual(self.s.isMatch('aa', '.*'), True)
    self.assertEqual(self.s.isMatch('aab', '.*'), True)
    self.assertEqual(self.s.isMatch('aab', 'c*a*b*'), True)
    self.assertEqual(self.s.isMatch('abab', '.*b*'), True)
    self.assertEqual(self.s.isMatch('acab', '.*b'), True)
    self.assertEqual(self.s.isMatch('ababc', '.*b'), False) 
    self.assertEqual(self.s.isMatch('ababc', '.*b.*'), True)
    self.assertEqual(self.s.isMatch('ababc', '.*b.*b.*c'), True)


if __name__ == "__main__":
  unittest.main()
