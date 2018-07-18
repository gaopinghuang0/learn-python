import unittest

# beats 100%
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # idea: the longer string would always be uncommon subsequence
        # if their length is equal, and if they do not equal,
        # then itself would be the longest uncommon subsequence
        # if they are equal, no uncommon subsequence
        m, n = len(a), len(b)
        if m != n:
            return max(m, n)
        if a == b:
            return -1
        return m


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.findLUSlength("aba", "cdc"), 3)


if __name__ == "__main__":
    unittest.main()
