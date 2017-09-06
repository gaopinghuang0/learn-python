import unittest


class Solution(object):
  LESS_THAN_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
  'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
  TENS = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
  
  def numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
      return 'Zero'

    thousands = ['', 'Thousand', 'Million', 'Billion']
    res = ''
    i = 0
    while num:
      temp = num % 1000
      if temp:
        res = self.helper(temp) + thousands[i] + ' ' + res
      i += 1
      num = num // 1000

    return res.strip()

  def helper(self, num):
    if num == 0:
      return ''
    elif num < 20:
      return self.LESS_THAN_20[num] + ' '
    elif num < 100:
      return self.TENS[num//10] + ' ' + self.helper(num % 10)
    else:
      return self.LESS_THAN_20[num//100] + ' Hundred ' + self.helper(num % 100)


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
    # most important case
    self.assertEqual(self.s.numberToWords(1100000010), 'One Billion One Hundred Million Ten')


if __name__ == "__main__":
  unittest.main()
