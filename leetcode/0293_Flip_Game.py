import unittest

# beats 100%
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                res.append(s[:i]+'--'+s[i+2:])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.generatePossibleNextMoves("++++"), ["--++", "+--+", "++--"])


if __name__ == "__main__":
    unittest.main()
