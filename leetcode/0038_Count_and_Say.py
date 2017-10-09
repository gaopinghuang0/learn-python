import unittest


class Solution(object):
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    ans = '1'
    for i in range(n-1):
      t = ''
      j = 1
      c = 1
      while j < len(ans):
        if ans[j] == ans[j-1]:
          c += 1
        else:
          t += str(c) + ans[j-1]
          c = 1
        j += 1
      t += str(c) + ans[j-1]
      ans = t
    return ans


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
