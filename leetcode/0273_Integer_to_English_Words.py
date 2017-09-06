import unittest


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = str(num)
        size = len(num)
        if size <= 3:
            res = self.three(num)
        elif size <= 6:
            res = self.six(num)
        elif size <= 9:
            res = self.nine(num)
        else:
            res = self.twelve(num)
        return res

    def twelve(self, num):
        if int(num[-9:]) == 0:
            return self.three(num[:-9]) + " Billion"
        if int(num[:-9]) == 0:
            return self.nine(num[-9:])
        return self.three(num[:-9]) + " Billion " + self.nine(num[-9:])

    def nine(self, num):
        if int(num[-6:]) == 0:
            return self.three(num[:-6]) + " Million"
        if int(num[:-6]) == 0:
            return self.six(num[-6:])
        return self.three(num[:-6]) + " Million " + self.six(num[-6:])
    
    def six(self, num):
        if int(num[-3:]) == 0:
            return self.three(num[:-3]) + " Thousand"
        if int(num[:-3]) == 0:
            return self.three(num[-3:])
        return self.three(num[:-3]) + " Thousand " + self.three(num[-3:])
        
    def three(self, num):
        # print (num)
        assert len(num) <= 3
        num = str(int(num))
        if int(num) >= 100:
            if int(num[1:]) == 0:
                return self.one(num[0]) + " Hundred"
            return self.one(num[0]) + " Hundred " + self.two(num[1:])
        elif int(num) >= 10:
            return self.two(num)
        else:
            return self.one(num)

    def two(self, num):
        ten = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        if int(num) >= 10:
            if num[0] == "1":
                return ten[int(num[1])]
            elif num[1] == '0':
                return tens[int(num[0])]
            else:
                return tens[int(num[0])] + " " + self.one(num[1])
        else:
            return self.one(num[1])
        
    def one(self, num):
        seed = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        assert len(num) == 1
        return seed[int(num)]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.numberToWords(0), 'Zero')
    self.assertEqual(self.s.numberToWords(10), 'Ten')
    self.assertEqual(self.s.numberToWords(123), 'One Hundred Twenty Three')
    self.assertEqual(self.s.numberToWords(11345), 'Eleven Thousand Three Hundred Forty Five')
    self.assertEqual(self.s.numberToWords(12345), 'Twelve Thousand Three Hundred Forty Five')
    self.assertEqual(self.s.numberToWords(1234567), 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')
    self.assertEqual(self.s.numberToWords(1000010), 'One Million Ten')
    self.assertEqual(self.s.numberToWords(1000000010), 'One Billion Ten')
    self.assertEqual(self.s.numberToWords(1100000010), 'One Billion One Hundred Million Ten')


if __name__ == "__main__":
  unittest.main()
