import unittest

# optimize a little by using global memo, beats 32.94%
class Solution(object):
    memo = {}
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # input is within 1 to 3999
        symbols = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        def convert(x, base):
            if (x,base) in self.memo:
                return self.memo[x,base]
            if x == 0:
                ans = ''
            elif 1 <= x <= 3:
                ans = symbols[base]*x
            elif x == 4:
                ans = symbols[base]+symbols[5*base]
            elif 5 <= x <= 8:
                ans = symbols[5*base]+symbols[base]*(x - 5)
            elif x == 9:
                ans = symbols[base]+symbols[10*base]
            self.memo[(x,base)] = ans
            return ans

        res = ''
        base = 1
        while num:
            res = convert(num % 10, base) + res
            num = num // 10
            base = base * 10

        return res

# beats 28.95%
class Solution_V1(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # input is within 1 to 3999
        symbols = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        def convert(x, base):
            if x == 0:
                return ''
            elif 1 <= x <= 3:
                return symbols[base]*x
            elif x == 4:
                return symbols[base]+symbols[5*base]
            elif 5 <= x <= 8:
                return symbols[5*base]+symbols[base]*(x - 5)
            elif x == 9:
                return symbols[base]+symbols[10*base]
        res = ''
        base = 1
        while num:
            res = convert(num % 10, base) + res
            num = num // 10
            base = base * 10

        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.intToRoman(3), 'III')
        self.assertEqual(self.s.intToRoman(4), 'IV')
        self.assertEqual(self.s.intToRoman(9), 'IX')
        self.assertEqual(self.s.intToRoman(58), 'LVIII')
        self.assertEqual(self.s.intToRoman(60), 'LX')
        self.assertEqual(self.s.intToRoman(1994), 'MCMXCIV')
        self.assertEqual(self.s.intToRoman(3094), 'MMMXCIV')


if __name__ == "__main__":
    unittest.main()
