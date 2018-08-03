import unittest

# beats 97.82%
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # idea: since matrix[0][0] will always be inc, then just count the min range
        min_a = m
        min_b = n
        for (a, b) in ops:
            if a < min_a:
                min_a = a
            if b < min_b:
                min_b = b
        return min_a * min_b

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.maxCount(3,3,[[2,2],[3,3]]), 4)


if __name__ == "__main__":
    unittest.main()
