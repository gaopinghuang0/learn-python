import unittest

# beats 99.71%
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cache = {}
        for c in s:
            if c in cache:
                del cache[c]
            else:
                cache[c] = True
        return len(cache) <= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.canPermutePalindrome('code'), False)
        self.assertEqual(self.s.canPermutePalindrome('aa'), True)
        self.assertEqual(self.s.canPermutePalindrome('aab'), True)
        self.assertEqual(self.s.canPermutePalindrome('carerac'), True)


if __name__ == "__main__":
    unittest.main()
