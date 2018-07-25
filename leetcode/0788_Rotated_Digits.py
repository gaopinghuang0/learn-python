import unittest

# beats 92.99%
class Solution(object):
    cache = {}
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N+1):
            if i in Solution.cache:
                if Solution.cache[i]:
                    count += 1
            else:
                valid = self.isvalid(i)
                Solution.cache[i] = valid
                if valid:
                    count += 1
        return count

    def isvalid(self, x):
        might = False
        for c in str(x):
            if c in '018':
                continue
            elif c in '2569':
                might = True
            else:
                return False
        return might



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.rotatedDigits(2), 1)
        self.assertEqual(self.s.rotatedDigits(10), 4)
        self.assertEqual(self.s.rotatedDigits(20), 9)
        self.assertEqual(self.s.rotatedDigits(857), 247)


if __name__ == "__main__":
    unittest.main()
