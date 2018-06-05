import unittest

import math
# idea from Submission, beats 97.66%
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        digits = range(1, n+1)
        res = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            res += str(digits.pop(index)) # remove handled digit
        return res


# too slow
from itertools import permutations
class Solution_Slow(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # compute factorial of n-1
        m = 1
        for i in range(1, n):
            m *= i
        # get the ith digit
        ith = k // m
        if k % m == 0:
            ith -= 1
        # move the ith digit to the beginning
        digits = [str(ith+1)] + [str(i+1) for i in range(n) if i != ith]
        i = k - m*ith - 1
        for s in permutations(digits[1:]):
            if i == 0:
                return digits[0] + ''.join(s)
            i -= 1
        return digits[0] + ''.join(s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.getPermutation(3,3), "213")
        self.assertEqual(self.s.getPermutation(3,4), "231")
        self.assertEqual(self.s.getPermutation(3,5), "312")
        self.assertEqual(self.s.getPermutation(4,9), "2314")


if __name__ == "__main__":
    unittest.main()
