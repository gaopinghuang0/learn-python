import unittest

# beats 38.07%
from collections import defaultdict
from heapq import *
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # idea: use a max heap to store all possible combinations
        # start from the largest
        if not words:
            return 0
        words = set(words)
        lookup = defaultdict(list)
        for word in words:
            lookup[len(word)].append(set(word))
        # print(lookup)
        hp = []
        for len1 in lookup:
            for len2 in lookup:
                if len1 < len2:
                    continue
                if len1 == len2 and len(lookup[len1]) <= 1:
                    continue
                heappush(hp, (-len1*len2, len1, len2))
        while hp:
            product, len1, len2 = heappop(hp)
            product = -product
            for word1_set in lookup[len1]:
                for word2_set in lookup[len2]:
                    # no common letters
                    if word1_set.isdisjoint(word2_set):
                        return product
        return 0


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    self.assertEqual(self.s.maxProduct(words), 16)
    


if __name__ == "__main__":
  unittest.main()
