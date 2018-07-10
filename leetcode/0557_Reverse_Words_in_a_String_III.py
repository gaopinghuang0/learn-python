import unittest

# beats 99.47%
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([subs[::-1] for subs in s.split(' ')])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")


if __name__ == "__main__":
    unittest.main()
