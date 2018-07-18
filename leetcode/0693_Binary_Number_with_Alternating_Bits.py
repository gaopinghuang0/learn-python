import unittest

# beats 92.63%
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # idea: get the binary format and then compare each pair
        s = bin(n)[2:]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.hasAlternatingBits(5), True)
        self.assertEqual(self.s.hasAlternatingBits(7), False)
        self.assertEqual(self.s.hasAlternatingBits(11), False)
        self.assertEqual(self.s.hasAlternatingBits(10), True)


if __name__ == "__main__":
    unittest.main()
