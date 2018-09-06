import unittest

# idea from Discuss
# https://leetcode.com/problems/count-primes/discuss/153528/Python3-99-112-ms-Explained:-The-Sieve-of-Eratosthenes-with-optimizations
# beats 98.42%
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea: dp
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                prime[i*i:n:i] = [0]*((n-1-i*i)//i + 1)
        return sum(prime)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.countPrimes(2), 0)
        self.assertEqual(self.s.countPrimes(3), 1)
        self.assertEqual(self.s.countPrimes(10), 4)


if __name__ == "__main__":
    unittest.main()
