import unittest


class Solution(object):
    def hammingWeight2(self, n):
        return bin(n).count('1')

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        # if n == 0:
        #     return 0
        while n != 0:
            n, m = divmod(n, 2)
            res += m
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        for i in xrange(10000):
            if self.s.hammingWeight(i) != self.s.hammingWeight2(i):
                print i


if __name__ == "__main__":
    unittest.main()
