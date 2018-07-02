import unittest

# optimize, beats 79.17%
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('U') == moves.count('D')) \
            and (moves.count('L') == moves.count('R'))

# beats 59.02%
import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # idea: the # of up should equal to # of down, similar for left-vs-right
        counter = collections.Counter(moves)
        return counter['U'] == counter['D'] and counter['L'] == counter['R']


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
