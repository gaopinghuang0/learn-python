import unittest

# beats 3.45%
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # idea: find the last 'D', reverse
        res = [1]
        i = 0
        n = len(s)
        while i < n:
            cnt = 0
            while i < n and s[i] == 'D':
                i += 1
                cnt += 1
                res.append(i+1)
            res = res[:i-cnt] + res[i-cnt:][::-1]
            while i < n and s[i] == 'I':
                i += 1
                res.append(i+1)
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.findPermutation('I'), [1,2])
        self.assertEqual(self.s.findPermutation('DI'), [2,1,3])
        self.assertEqual(self.s.findPermutation('DDI'), [3,2,1,4])
        self.assertEqual(self.s.findPermutation('DDIID'), [3,2,1,4,6,5])
        self.assertEqual(self.s.findPermutation('DDIIDD'), [3,2,1,4,7,6,5])
        self.assertEqual(self.s.findPermutation('DDIIIDD'), [3,2,1,4,5,8,7,6])
        self.assertEqual(self.s.findPermutation('DDIIDI'), [3,2,1,4,6,5,7])


if __name__ == "__main__":
    unittest.main()
