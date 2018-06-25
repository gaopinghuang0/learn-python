import unittest


# idea from Discuss, beats 17.30%
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # idea from Discuss, use a dict to store the num and index,
        # if we meet the same num, return
        # https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51106/My-clean-Java-solution
        if numerator == 0:
            return '0'
        res = []
        # sign
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)

        # int part
        res.append(str(numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return ''.join(res)

        # fraction part
        res.append('.')
        cache = {}  # {numerator: index}
        cache[numerator] = len(res)
        while numerator != 0:
            numerator *= 10
            res.append(str(numerator // denominator))
            numerator %= denominator
            if numerator in cache:  # found repeat
                res.append(')')
                index = cache[numerator]
                res.insert(index, '(')
                break
            else:
                cache[numerator] = len(res)
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.fractionToDecimal(0, 2), '0')
        self.assertEqual(self.s.fractionToDecimal(1, 2), '0.5')
        self.assertEqual(self.s.fractionToDecimal(1, -2), '-0.5')
        self.assertEqual(self.s.fractionToDecimal(2, 1), '2')
        self.assertEqual(self.s.fractionToDecimal(2, 3), '0.(6)')
        self.assertEqual(self.s.fractionToDecimal(2, 30), '0.0(6)')
        self.assertEqual(self.s.fractionToDecimal(1, 7), '0.(142857)')
        self.assertEqual(self.s.fractionToDecimal(1, 70), '0.0(142857)')



if __name__ == "__main__":
    unittest.main()
