import unittest


# idea from Discuss, beats 61.63%
# https://leetcode.com/problems/integer-replacement/discuss/87920/A-couple-of-Java-solutions-with-explanations
class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea from Discuss:
        # if n is even, halve it
        # if n=3 or n-1 has less 1's than n+1, decrement n
        # otherwise increment n
        # even further, for odd n:
        # if the last two bits are 01, then decrement
        # if they are 11, increment
        count = 0
        while n != 1:
            if n & 1 == 0:  # even
                n >>= 1
            elif (n == 3) or (n & 2 == 0):
                n -= 1
            else:
                n += 1
            count += 1
        return count

class Solution_Wrong:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea: bit operation, find the position of the most significant 1
        # plus the # of 1s on its right
        byte = bin(n)[2:]
        print(byte)
        return (len(byte) - 1) + (byte.count('1') - 1)
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.integerReplacement(8), 3)
        self.assertEqual(self.s.integerReplacement(7), 4)
        self.assertEqual(self.s.integerReplacement(1), 0)
        self.assertEqual(self.s.integerReplacement(2), 1)
        self.assertEqual(self.s.integerReplacement(65535), 17)


if __name__ == "__main__":
    unittest.main()
