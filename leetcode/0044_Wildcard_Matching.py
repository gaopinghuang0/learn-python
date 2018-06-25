import unittest

# beats 55.65%
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # idea: 2D dp
        # similar to 0010_Regular_Expression_Matching
        # dp[i][j] for s[:i] and p[:j]
        m, n = len(s)+1, len(p)+1
        matches = [[False]*n for _ in range(m)]

        # match two empty input
        matches[0][0] = True

        # match empty s with *, **, or more *
        for i, elem in enumerate(p, 1):
            matches[0][i] = matches[0][i-1] and elem == '*'

        # print(matches)
        for i, ss in enumerate(s, 1):
            for j, pp in enumerate(p, 1):
                if pp != '*':
                    matches[i][j] = matches[i-1][j-1] and (ss == pp or pp == '?')
                else:
                    matches[i][j] = matches[i-1][j] or matches[i][j-1]
        # print(matches)
        return matches[-1][-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.isMatch('aa', 'a'), False)
        self.assertEqual(self.s.isMatch('aa', '*'), True)
        self.assertEqual(self.s.isMatch('aa', '**'), True)
        self.assertEqual(self.s.isMatch('aa', '***'), True)
        self.assertEqual(self.s.isMatch('cb', '?a'), False)
        self.assertEqual(self.s.isMatch('adceb', '*a*b'), True)
        self.assertEqual(self.s.isMatch('acdcb', 'a*c?b'), False)


if __name__ == "__main__":
    unittest.main()
