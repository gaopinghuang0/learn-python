import unittest

# Check the solution: https://leetcode.com/problems/longest-palindromic-substring/solution/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in xrange(len(s)):
            len1 = self.extendPalindromeFromCenter(s, i, i)  # for odd length
            len2 = self.extendPalindromeFromCenter(s, i, i+1)  # for even length
            currLen = max(len1, len2)
            if currLen > end-start:
                start = i - (currLen-1)/2
                end = i + currLen/2
        return s[start:end+1]

    def extendPalindromeFromCenter(self, s, L, R):
        while L >= 0 and R <= len(s)-1 and s[L] == s[R]:
            L -= 1
            R += 1
        return R-L-1




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertTrue(self.s.longestPalindrome('a') in ['a'])
        self.assertTrue(self.s.longestPalindrome('babad') in ['aba', 'bab'])
        print self.s.longestPalindrome('bacacab')
        self.assertTrue(self.s.longestPalindrome('bacacab') in ['bacacab'])


if __name__ == "__main__":
    unittest.main()
