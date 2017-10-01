import unittest

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# my own implementation of read4
data = list(range(11))
c = 0
def read4(buf):
  global c
  if c < len(data):
    temp = data[c:c+4]
  else:
    temp = []
  c += len(temp)
  for i in range(len(temp)):
    buf[i] = temp[i]
  return len(temp)

class Solution(object):
  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    # note: the read() function will be called only once
    # therefore, there is no need to store read4() data
    res = []
    idx = 0
    while True:
      temp = [""]*4
      m = read4(temp)
      curr = min(n-idx, m)
      for i in range(curr):
        buf[idx] = temp[i]
        idx += 1
      if curr < 4:
        break
    return idx


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    global c
    n = 10
    buf = ['']*n
    self.assertEqual(self.s.read(buf, n), n)

    c = n
    n = 4
    buf = ['']*n
    self.assertEqual(self.s.read(buf, n), 1)



if __name__ == "__main__":
  unittest.main()
