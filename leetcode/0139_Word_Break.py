import unittest

# update: my new faster version, beats 99.95%
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # idea: 1D dp, ok[i] means s[:i] can be built
        if not wordDict:
            return False
        words = set(wordDict)
        word_lens = {len(x)-1 for x in words}
        ok = [True]
        for i in range(len(s)):
            ok.append(any((i-j>=0 and ok[-1-j] and s[i-j:i+1] in words) for j in word_lens))
        return ok[-1]



class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # idea: ok[i] tells whether s[:i] can be built
    ok = [True]
    wordDict = set(wordDict)
    if not wordDict:
      return False
    max_len = len(max(wordDict, key=len))
    for i in range(len(s)):
      ok.append(any((i-j>=0 and ok[-1-j] and s[i-j:i+1] in wordDict) for j in range(max_len)))
    return ok[-1]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.wordBreak('a', ['a']), True)
    self.assertEqual(self.s.wordBreak('a', []), False)
    self.assertEqual(self.s.wordBreak('abcd', ['a', 'abc', 'b', 'cd']), True)
    self.assertEqual(self.s.wordBreak('le', ['l', 'e']), True)
    self.assertEqual(self.s.wordBreak('let', ['le', 'e', 'te']), False)
    self.assertEqual(self.s.wordBreak('l', ['leet', 'code']), False)
    self.assertEqual(self.s.wordBreak('leetcode', ['leet', 'code']), True)


if __name__ == "__main__":
  unittest.main()
