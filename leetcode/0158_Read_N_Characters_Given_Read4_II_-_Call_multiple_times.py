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

# update: my new own version, shortest and fastest
class Solution(object):
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # idea: store the data from read4() for future use
        # note: update buf in-place
        while len(self.queue) < n:
            tmp = [""]*4
            read4(tmp)
            self.queue.extend(tmp)
            
        for i in range(n):
            buf[i] = self.queue.popleft()
        return n


class Solution(object):
  def __init__(self):
    self.queue = []

  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    # note: cannot use len(buf) or len(temp) to get the length
    # because they should be fixed-length buffers
    # note2: the read() function could be called for many times, therefore,
    # the read4() chars need to be stored for future use
    idx = 0
    while 1:
      temp = [""]*4
      m = read4(temp)
      self.queue += temp
      curr = min(n-idx, len(self.queue))
      for i in range(curr):
        buf[idx] = self.queue.pop(0)
        idx += 1
      if curr == 0:  # end of file or read n char already
        break
    return idx




class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    buf = [""]
    self.assertEqual(self.s.read(buf, 0), 0)
    print(buf)

    buf = [""]*1
    self.assertEqual(self.s.read(buf, 1), 1)
    print(buf)

    buf = [""]
    self.assertEqual(self.s.read(buf, 0), 0)
    print(buf)

    buf = [""]*5
    self.assertEqual(self.s.read(buf, 5), 5)
    print(buf)

if __name__ == "__main__":
  unittest.main()
