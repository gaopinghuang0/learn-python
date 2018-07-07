import unittest


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)[2:]
        return int(''.join(['1' if i == '0' else '0' for i in binary]), 2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.findComplement(5), 2)
        self.assertEqual(self.s.findComplement(1), 0)


if __name__ == "__main__":
    unittest.main()
