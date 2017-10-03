import unittest


class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    m = len(s)
    n = len(t)
    if abs(m-n) > 1:
      return False
    if m == n:  # check if one char different
      count = 0
      for i, j in zip(s,t):
        if i != j:
          count += 1
      return count == 1
    if m == 0 or n == 0:
      return True
    if m < n:
      m, n, s, t = n, m, t, s
    # now t is shorter
    count, i, j = 0, 0, 0
    while i < n:
      if t[i] != s[j]:
        j += 1
        count += 1
      else:
        i += 1
        j += 1
      if j >= m and count != 1:
        return False
    if j < m and count == 0:
      return True
    return count == 1


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
