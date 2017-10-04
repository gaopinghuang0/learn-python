import unittest


# note: empty string is valid
# only alphanumeric
# case insensitive
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
          return True

        s = [x for x in s.lower() if x.isalnum()]
        return s == s[::-1]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.isPalindrome(""), True)
    self.assertEqual(self.s.isPalindrome("race a car"), False)
    self.assertEqual(self.s.isPalindrome("A man, a plan, a canal: Panama"), True)


if __name__ == "__main__":
  unittest.main()
