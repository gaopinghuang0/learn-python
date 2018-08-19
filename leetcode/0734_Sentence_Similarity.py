import unittest

# beats 98.59%
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # idea: use a dict to store pairs?
        if len(words1) != len(words2):
            return False

        lookup = set()
        for pair in pairs:
            lookup.add('-'.join(sorted(pair)))
        for pair in zip(words1, words2):
            if pair[0] == pair[1]:
                continue
            key = '-'.join(sorted(pair))
            if key not in lookup:
                return False
        return True



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        words1 = ['great']
        words2 = ['great']
        pairs = []
        self.assertEqual(self.s.areSentencesSimilar(words1, words2, pairs), True)

        words1 = ["an","extraordinary","meal"]
        words2 = ["a","good","dinner"]
        pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
        self.assertEqual(self.s.areSentencesSimilar(words1, words2, pairs), False)


if __name__ == "__main__":
    unittest.main()
