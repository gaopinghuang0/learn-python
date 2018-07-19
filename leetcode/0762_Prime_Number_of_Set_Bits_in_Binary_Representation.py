import unittest

# beats 95.04%
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = set([2,3,5,7,11,13,17,19,21])
        count = 0
        for i in range(L, R+1):
            if bin(i)[2:].count('1') in prime:
                count += 1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.countPrimeSetBits(6, 10), 4)
        self.assertEqual(self.s.countPrimeSetBits(10, 15), 5)


if __name__ == "__main__":
    unittest.main()
