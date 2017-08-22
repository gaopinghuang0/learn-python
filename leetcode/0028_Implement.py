import unittest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
        	return 0
        if not haystack:
        	return -1
        nsize = len(needle)
        hsize = len(haystack)
        if nsize > hsize:
        	return -1

        for i in xrange(hsize-nsize+1):
        	if haystack[i:i+nsize] == needle:
        		return i
       	return -1
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.strStr('', ''), 0)
        self.assertEqual(self.s.strStr('a', ''), 0)
        self.assertEqual(self.s.strStr('a', 'a'), 0)
        self.assertEqual(self.s.strStr('a', 'ab'), -1)
        self.assertEqual(self.s.strStr('abc', 'a'), 0)
        self.assertEqual(self.s.strStr('aaabbbccc', 'abb'), 2)
        self.assertEqual(self.s.strStr('aaabbbccc', 'bbc'), 4)
        self.assertEqual(self.s.strStr('aaabbbccc', 'bbcc'), 4)
        self.assertEqual(self.s.strStr('aaabbbccc', 'bbd'), -1)
        self.assertEqual(self.s.strStr('aaabbbccc', 'ccc'), 6)


if __name__ == "__main__":
    unittest.main()
