import unittest

# beats 50.24%
import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = re.sub(r'\s+', ' ', s.strip()).split(' ')
        return ' '.join(words[::-1])



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(self.s.reverseWords(" the  sky   is blue  "), "blue is sky the")


if __name__ == "__main__":
    unittest.main()
