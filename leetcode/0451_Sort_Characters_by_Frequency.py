import unittest

import collections
# beats 33%
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        return ''.join(key*cnt for key, cnt in counter.most_common())

# beats 55.88%
class Solution_V1(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        res = ''
        for key, cnt in counter.most_common():
            res += key*cnt
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertTrue(self.s.frequencySort('cccaaa') in ['cccaaa', 'aaaccc'])
        self.assertTrue(self.s.frequencySort('tree') in ['eert', 'eetr'])
        self.assertTrue(self.s.frequencySort('Aabb') in ['bbAa', 'bbaA'])


if __name__ == "__main__":
    unittest.main()
