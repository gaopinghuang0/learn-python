import unittest

# modifed based on 
# https://discuss.leetcode.com/topic/30308/my-clear-java-solution-with-explanation
class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    m = len(s)
    n = len(t)
    for i in range(min(m,n)):
      if s[i] != t[i]:
        # three possibilities
        if m == n:  # compare rest
          return s[i+1:] == t[i+1:]
        elif m < n:  # delete one char from t
          return s[i:] == t[i+1:]
        else:  # delete one char from s
          return s[i+1:] == t[i:]
    return abs(m - n) == 1  # all previous chars are the same, check extra chars

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.isOneEditDistance('', ''), False)
    self.assertEqual(self.s.isOneEditDistance('', '23'), False)
    self.assertEqual(self.s.isOneEditDistance('', '2'), True)
    self.assertEqual(self.s.isOneEditDistance('3', '23'), True)
    self.assertEqual(self.s.isOneEditDistance('123', '23'), True)
    self.assertEqual(self.s.isOneEditDistance('123', '234'), False)
    self.assertEqual(self.s.isOneEditDistance('123', '1234'), True)
    self.assertEqual(self.s.isOneEditDistance('123', '1244'), False)
    self.assertEqual(self.s.isOneEditDistance('4123', '123'), True)
    self.assertEqual(self.s.isOneEditDistance('123', '13'), True)


if __name__ == "__main__":
  unittest.main()
