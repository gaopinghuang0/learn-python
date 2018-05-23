import unittest


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # idea: recursion from right to left
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = self.grayCode(n-1)
        # add 2**(n-1) to the reverse of half
        return res + [2**(n-1)+x for x in res[::-1]]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.grayCode(2), [0,1,3,2])
        self.assertEqual(self.s.grayCode(3), [0,1,3,2,6,7,5,4])


if __name__ == "__main__":
    unittest.main()
