import unittest


# idea: Trie tree, each children is 26 fixed length
from collections import defaultdict
class TrieNode(object):
  def __init__(self):
    self.is_word = False
    self.children = defaultdict(TrieNode)

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
          node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _search(node, word):
          for i, c in enumerate(word):
            if c == '.':
              if i == len(word) - 1:
                return any(n.is_word for n in node.children.values())
              return any(_search(n, word[i+1:]) for n in node.children.values())
            else:
              if c in node.children:
                node = node.children[c]
              else:
                return False
          return node.is_word

        return _search(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dab')
obj.addWord('a')
obj.addWord('mad')
print(obj.search('bad'))
print(obj.search('.b'))
print(obj.search('.b.'))
print(obj.search('.'))
print(obj.search('ba..'))

# class TestSolution(unittest.TestCase):
#   def setUp(self):
#     self.s = Solution()

#   def test_method(self):
#     """Such as self.assertEqual, self.assertTrue"""
#     self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
  # unittest.main()
  pass
