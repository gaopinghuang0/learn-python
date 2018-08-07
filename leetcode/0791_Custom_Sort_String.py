import unittest

# beats 100%
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # idea: use index as value, 0 by default
        order = [0]*26
        for i,c in enumerate(S):
            order[ord(c)-97] = i
        return ''.join(sorted(T, key=lambda c: order[ord(c)-97]))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.customSortString("cba", 'abcd'), 'cdba')
        self.assertEqual(self.s.customSortString("jftiugkz", 'kfiukutzjg'), 'jftiuugkkz')


if __name__ == "__main__":
    unittest.main()
