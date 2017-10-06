import unittest


class Solution(object):
  def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    def digit_multiply(digit, offset):
        if digit in cache:
          ans = cache[digit]
        else:
          ans = 0
          for x in num1_rev:
            ans += digit * x
          cache[digit] = ans
        return ans * (10 ** offset)

    m = len(num1)
    n = len(num2)
    if not m or not n:
      return '0'
    num1_rev = [10**i * int(x) for i, x in enumerate(num1[::-1])]
    cache = {}
    ans = 0
    for i, digit in enumerate(num2):
      ans += digit_multiply(int(digit), n-i-1)
    return str(ans)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.multiply('11', ''), '0')
    self.assertEqual(self.s.multiply('11', '11'), '121')
    self.assertEqual(self.s.multiply('111', '11'), '1221')
    self.assertEqual(self.s.multiply('123', '456'), '56088')


if __name__ == "__main__":
  unittest.main()
