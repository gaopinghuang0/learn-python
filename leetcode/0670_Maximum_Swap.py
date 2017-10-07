import unittest

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # swap two digits or not
        # idea: two pointers
        s = list(str(num))
        n = len(s)
        if n <= 1:
            return num
        i = 0
        while i < n - 1:
            max_digit = max(s[i+1:])
            if max_digit <= s[i]:
                i += 1
            else:
                # find the max_digit and swap
                j = n - 1
                while j > i and s[j] != max_digit:
                    j -= 1
                s[i], s[j] = s[j], s[i]
                return int(''.join(s))
        return num








class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        pass


if __name__ == "__main__":
    unittest.main()
