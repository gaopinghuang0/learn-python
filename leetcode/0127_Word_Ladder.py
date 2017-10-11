import unittest

# bidirectional BFS
# Credit: https://discuss.leetcode.com/topic/19721/share-my-two-python-solutions-a-very-concise-one-12-lines-160ms-and-an-optimized-solution-100ms
# Credit: https://discuss.leetcode.com/topic/19721/share-my-two-python-solutions-a-very-concise-one-12-lines-160ms-and-an-optimized-solution-100ms/10#
import string
class Solution(object):
  def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    # All words have the same length.
    # You may assume no duplicates in the word list.
    # You may assume beginWord and endWord are non-empty and are not the same.
    wordList = set(wordList)
    if endWord not in wordList:
      return 0
    front = {beginWord}
    back = {endWord}
    ans = 1
    word_len = len(beginWord)
    while front:
      ans += 1
      next_front = set()
      for word in front:
        for i in range(word_len):
          for c in string.lowercase:
            if c != word[i]:
              new_word = word[:i]+c+word[i+1:]
              if new_word in back:
                return ans
              if new_word in wordList:
                next_front.add(new_word)
                wordList.remove(new_word)
      front = next_front
      if len(back) < len(front):
        front, back = back, front
    return 0



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
