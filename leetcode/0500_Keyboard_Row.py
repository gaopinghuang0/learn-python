import unittest

# beats 99.88%
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # idea: just use a dictionary
        lookup = {}
        for i, chars in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm']):
            for c in chars:
                lookup[c] = i
        res = []
        for word in words:
            if word:
                prev = lookup[word[0].lower()]
            else:
                continue
            valid = True
            for c in word[1:]:
                if lookup[c.lower()] != prev:
                    valid = False
                    break
            if valid:
                res.append(word)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])


if __name__ == "__main__":
    unittest.main()
