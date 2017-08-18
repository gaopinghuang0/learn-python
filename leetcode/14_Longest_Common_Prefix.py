import unittest


class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not len(strs):
      return ''
    i = 0
    first = strs[0]
    for c in first:
      if all(len(s) > i and s[i] == c for s in strs):
        i += 1
      else:
        break
    return strs[0][:i]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.longestCommonPrefix([]), '')
    self.assertEqual(self.s.longestCommonPrefix(['a', 'ab']), 'a')
    self.assertEqual(self.s.longestCommonPrefix(['abc', 'ab']), 'ab')
    self.assertEqual(self.s.longestCommonPrefix(['abc', 'ab', 'ac']), 'a')
    self.assertEqual(self.s.longestCommonPrefix(['abc', 'ab', 'bc']), '')


if __name__ == "__main__":
  unittest.main()
