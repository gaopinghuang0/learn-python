import unittest

# beats 75.54%
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        queue = ['({},{})'.format(i,n-i+1) for i in range(1, n//2+1)]
        while len(queue) > 1:
            n = len(queue)
            queue = ['({},{})'.format(queue[i],queue[n-i-1]) for i in range(n//2)]
        return queue[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.findContestMatch(2), '(1,2)')
        self.assertEqual(self.s.findContestMatch(4), '((1,4),(2,3))')
        self.assertEqual(self.s.findContestMatch(8), '(((1,8),(4,5)),((2,7),(3,6)))')


if __name__ == "__main__":
    unittest.main()
