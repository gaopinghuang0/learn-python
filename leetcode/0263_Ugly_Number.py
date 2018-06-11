import unittest

# beats 78.37%
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num%i == 0:
                num /= i
        return num == 1

class Solution_V1(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        for x in (10,8,6,5,4,3,2):
            while num % x == 0:
                num = num / x

        return num == 1

class Solution_TooSlow(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = remove(num, 2)
        num = remove(num, 3)
        num = remove(num, 5)

        return num == 1
        
def remove(num, factor):
    while num % factor == 0:
        num = num / factor
    return num

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
