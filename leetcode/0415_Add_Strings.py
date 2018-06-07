import unittest

# beats 62.45%
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # make sure num1 is longer, or m is larger
        m, n = len(num1), len(num2)
        if m < n:
            num1, num2 = num2, num1
            m, n = n, m
        carry = 0
        res = ''

        for i in range(1, n+1):
            s = int(num2[-i]) + int(num1[-i]) + carry
            carry = 1 if s >= 10 else 0
            res = str(s % 10) + res

        for i in range(m-n)[::-1]:
            s = int(num1[i]) + carry
            carry = 1 if s >= 10 else 0
            res = str(s % 10) + res

        if carry:
            res = '1' + res
            
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.addStrings("199", "9"), '208')
        self.assertEqual(self.s.addStrings("109", "9"), '118')
        self.assertEqual(self.s.addStrings("100", "9"), '109')
        self.assertEqual(self.s.addStrings("9", "99"), '108')


if __name__ == "__main__":
    unittest.main()
