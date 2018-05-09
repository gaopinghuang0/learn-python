import unittest

# idea from Submission,  only beats 8.81%
# why it is slower than the solution below?
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # idea from Submission
        if n <= 0:
            return False
        return (n & n-1) == 0

# beats 81.01%
class Solution_V1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # idea: bit operation
        if n <= 0:
            return False
        has_one = False
        while n > 0:
            if n & 1:
                if has_one:
                    return False
                has_one = True
            n = n >> 1
        return has_one

class Solution_Slow(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # method 0, not OK because of float
        # from math import log
        # if n <= 0:
        #     return False
        # return log(n, 2) % 1 == 0
    
        # method 1
        while n>0 and n%2==0:
            n=n/2
        return (n==1)
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.isPowerOfTwo(2), True)
        self.assertEqual(self.s.isPowerOfTwo(-12), False)
        self.assertEqual(self.s.isPowerOfTwo(218), False)
        self.assertEqual(self.s.isPowerOfTwo(32), True)


if __name__ == "__main__":
    unittest.main()
