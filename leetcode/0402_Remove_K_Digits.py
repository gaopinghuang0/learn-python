import unittest

# beats 80.35%
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # idea: stack and move the larger digit from the beginning
        stack = []
        count = 0
        for d in num:
            if count < k and stack and stack[-1] > d:
                while stack:
                    last = stack[-1]
                    if last > d:
                        stack.pop()
                        count += 1
                        if count == k:
                            break
                    else:
                        break
            stack.append(d)
        if count < k:
            # stack must be in non-decreasing order, remove last few digits
            stack = stack[:-(k-count)]
        return ''.join(stack).lstrip('0') or '0'


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.removeKdigits('1432219', 3), '1219')
        self.assertEqual(self.s.removeKdigits('10200', 1), '200')
        self.assertEqual(self.s.removeKdigits('10', 2), '0')


if __name__ == "__main__":
    unittest.main()
