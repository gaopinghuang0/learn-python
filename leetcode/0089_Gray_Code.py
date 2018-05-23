import unittest

# beats 22.01%
# I don't know why it's slower than recursion
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # idea: iterative
        res = [0]
        for i in range(n):
            head = 1 << i
            res += [head+x for x in res[::-1]]
        return res

# beats 75.47%
class Solution_V1(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # idea: recursion from right to left
        if n == 0:
            return [0]
        res = self.grayCode(n-1)
        # add 2**(n-1) to the reverse of half
        head = 1 << (n-1)
        return res + [head+x for x in res[::-1]]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.grayCode(2), [0,1,3,2])
        self.assertEqual(self.s.grayCode(3), [0,1,3,2,6,7,5,4])


if __name__ == "__main__":
    unittest.main()
