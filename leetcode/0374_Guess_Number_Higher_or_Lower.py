import unittest


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


# the API above seems wrong
# beats 99.55%
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea: binary search
        lo = 1
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            res = guess(mid)
            if res == 1:
                lo = mid+1
            elif res == -1:
                hi = mid-1
            else:
                return mid
        return lo

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
