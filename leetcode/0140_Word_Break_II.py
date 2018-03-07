import unittest


# beats 46.30%
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # idea: use a Trie and a memo
        # build a Trie
        trie = {}
        for word in wordDict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]       
            t['#'] = True  # mark the end of a word
        memo = {}

        def _word_break(s, memo):
            if s in memo:
                return memo[s]
            t = trie
            res = []
            for i,c in enumerate(s):
                if c in t:
                    t = t[c]
                    if '#' in t:  # is a word
                        prefix = s[:i+1]
                        if prefix == s:
                            res.append(prefix)
                        else:
                            for rest in _word_break(s[i+1:], memo):
                                res.append(prefix + ' ' + rest)
                else:
                    break
            memo[s] = res
            return res

        return _word_break(s, memo)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(self.s.wordBreak(s, wordDict))


if __name__ == "__main__":
  unittest.main()
