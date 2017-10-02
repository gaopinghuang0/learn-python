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
    # do not add '+', '-', '*' before pos 0
    # the only possible operation is 'concat'
    # this for-loop handles the concat before pos
    # while the for-loop in dfs() handles concat after pos
    for pos in range(1, self.n+1):
      if pos > 1 and num[0] == '0': # avoid 00*
        break
      curr = int(num[:pos])
      self.dfs(num[:pos], pos, curr, curr)
    return self.res

  def dfs(self, path, pos, val, multed):
    if pos == self.n:
      if val == self.target:
        self.res.append(path)
    for i in range(pos+1, self.n+1):
      if i != pos+1 and self.num[pos] == '0':  
        break
      s = self.num[pos:i]
      curr = int(s)
      self.dfs(path+'+'+s, i, val+curr, curr)
      self.dfs(path+'-'+s, i, val-curr, -curr)
      self.dfs(path+'*'+s, i, val-multed+multed*curr, multed*curr)
    

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
