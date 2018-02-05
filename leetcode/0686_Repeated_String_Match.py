import unittest

# beats 98.07%
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for c in B:
            if c not in A:
                return -1
        m, n = len(A), len(B)
        for i in range(n//m, n//m+3):
            if B in A*i:
                return i
        return -1

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.repeatedStringMatch('abcd', 'cdab'), 2)
    self.assertEqual(self.s.repeatedStringMatch('abcd', 'cdabcdab'), 3)
    self.assertEqual(self.s.repeatedStringMatch("abababaaba", "aabaaba"), 2)


if __name__ == "__main__":
  unittest.main()
