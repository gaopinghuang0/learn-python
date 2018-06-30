import unittest

# beats no data
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[num^1 for num in row[::-1]] for row in A]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        inpt = [[1,1,0],[1,0,1],[0,0,0]]
        outp = [[1,0,0],[0,1,0],[1,1,1]]
        self.assertEqual(self.s.flipAndInvertImage(inpt), outp)
        inpt = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
        outp = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        self.assertEqual(self.s.flipAndInvertImage(inpt), outp)


if __name__ == "__main__":
    unittest.main()
