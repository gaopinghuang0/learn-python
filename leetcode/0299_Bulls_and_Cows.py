import unittest

# beats 98.09%
import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # the # of cows needs to consider the # of digits in secret
        secret_counter = collections.defaultdict(int)
        guess_counter = collections.defaultdict(int)
        bull, cow = 0, 0
        for x, y in zip(secret, guess):
            if x == y:
                bull += 1
            else:
                secret_counter[x] += 1
                guess_counter[y] += 1
        for y, count in guess_counter.items():
            cow += min(secret_counter[y], count)
        return '{}A{}B'.format(bull, cow)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        secret = "1807"
        guess = "7810"
        self.assertEqual(self.s.getHint(secret, guess), '1A3B')
        secret = "1123"
        guess = "0111"
        self.assertEqual(self.s.getHint(secret, guess), '1A1B')


if __name__ == "__main__":
    unittest.main()
