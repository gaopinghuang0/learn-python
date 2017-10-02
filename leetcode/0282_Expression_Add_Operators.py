import unittest

# modified from:
# https://discuss.leetcode.com/topic/24523/java-standard-backtrace-ac-solutoin-short-and-clear
class Solution(object):
  def addOperators(self, num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    self.num = num
    self.n = len(num)
    self.target = target
    self.res = []
    self.dfs("", 0, 0, 0)
    return self.res

  def dfs(self, path, pos, val, multed):
    if pos == self.n:
      if val == self.target:
        self.res.append(path)
    for i in range(pos+1, self.n+1):
      if i != pos+1 and self.num[pos] == '0':  # avoid 00*
        break

      curr = int(self.num[pos:i])
      # do not add '+', '-', '*' before pos 0
      # the only possible operation is 'concat'
      # also, since the for-loop guarantees that all possible concat after pos will be handled, 
      # then when pos != 0, we cannot concat path with curr again.
      # for example, num is '12345' and pos is 2, then the for-loop will call path on
      # '12->3', '12->34', and '12->345' in the subcalls, respectively.
      # Note that in the subcall of path '12->3', if we concat again,
      # we will get path '12->34', '12->345' again, which is duplicate 
      if pos == 0:
        self.dfs(path+str(curr), i, curr, curr)
      else:
        # self.dfs(path+str(curr), i, ..., ...)  # <-- note: cannot concat again
        self.dfs(path+'+'+str(curr), i, val+curr, curr)
        self.dfs(path+'-'+str(curr), i, val-curr, -curr)
        self.dfs(path+'*'+str(curr), i, val-multed+multed*curr, multed*curr)
      

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.addOperators("123", 6), ["1+2+3", "1*2*3"])
    self.assertEqual(self.s.addOperators("232", 8), ["2+3*2", "2*3+2"])
    self.assertEqual(self.s.addOperators("00", 0), ["0+0", "0-0", "0*0"])
    self.assertEqual(self.s.addOperators("3456237490", 9191), [])

if __name__ == "__main__":
  unittest.main()
