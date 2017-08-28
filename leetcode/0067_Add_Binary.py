import unittest


class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    len_a = len(a)
    len_b = len(b)
    c = 0
    res = ''
    i = -1
    while i >= -len_a or i >= -len_b or c > 0:
      v1 = v2 = 0
      if i >= -len_a:
        v1 = int(a[i])
      if i >= -len_b:
        v2 = int(b[i])
      val = v1 + v2 + c
      if val >= 2:
        res = str(val-2) + res
        c = 1
      else:
        res = str(val) + res
        c = 0
      i -= 1
    return res


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.addBinary('1', ''), '1')
    self.assertEqual(self.s.addBinary('1', '0'), '1')
    self.assertEqual(self.s.addBinary('11', '1'), '100')


if __name__ == "__main__":
  unittest.main()
