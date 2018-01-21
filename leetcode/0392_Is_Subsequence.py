import unittest


# beats 16.33%
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        i = 0
        for j in range(len(s)):
            while i < len(t) and t[i] != s[j]:
                i += 1
            if i >= len(t) and j < len(s):
                return False
            else:
                i += 1
        return True

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
