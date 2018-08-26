import unittest

# beats 98.14%
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # idea: one loop, save the mapping from s to t
        mapping = {}
        mapped = set()
        for x,y in zip(s, t):
            if x in mapping:
                if mapping[x] == y:
                    continue
                else:
                    return False
            elif y in mapped:
                return False
            else:
                mapping[x] = y
                mapped.add(y)
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        s = "egg"
        t = "add"
        self.assertEqual(self.s.isIsomorphic(s, t), True)
        s = "foo"
        t = "bar"
        self.assertEqual(self.s.isIsomorphic(s, t), False)
        s = "paper"
        t = "title"
        self.assertEqual(self.s.isIsomorphic(s, t), True)
        s = "ab"
        t = "aa"
        self.assertEqual(self.s.isIsomorphic(s, t), False)
        s = "ba"
        t = "aa"
        self.assertEqual(self.s.isIsomorphic(s, t), False)

if __name__ == "__main__":
    unittest.main()
