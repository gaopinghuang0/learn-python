import unittest

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# my own implementation of read4
data = list(range(11))
data = ['a']
c = 0
def read4(buf):
  global c
  temp = data[c:c+4]
  buf += temp
  c += len(temp)
  return len(temp)

class Solution(object):
  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    while 1:
      temp = []
      m = read4(temp)
      i = min(n - len(buf), m)
      buf += temp[:i]
      if i < 4:  # end of file or read n char already
        break
    return len(buf)

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    global c
    c = 0
    buf = []
    self.assertEqual(self.s.read(buf, 12), 11)
    print(buf)

    c = 0
    buf = []
    self.assertEqual(self.s.read(buf, 11), 11)
    print(buf)

    c = 0
    buf = []
    self.assertEqual(self.s.read(buf, 7), 7)
    print(buf)

if __name__ == "__main__":
  unittest.main()
