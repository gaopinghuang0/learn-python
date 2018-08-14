import unittest


# beats 100%
# idea: use the length as the key of a dict
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = collections.defaultdict(set)  # {word_len: set(word)}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        # reset here
        self.dictionary = collections.defaultdict(set)
        for word in dict:
            self.dictionary[len(word)].add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for saved_word in self.dictionary.get(len(word), []):
            if self.distance_one(word, saved_word):
                return True
        return False

    def distance_one(self, word, saved_word):
        for i in range(len(word)):
            if word[i] == saved_word[i]:
                continue
            else:
                return word[i+1:] == saved_word[i+1:]
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
