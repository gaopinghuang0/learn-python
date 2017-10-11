import unittest

class Solution(object):
  def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    # idea: DFS
    stack = []
    m = len(rooms)
    if rooms:
      n = len(rooms[0])
    # find all 0s
    for i in range(m):
      for j in range(n):
        if rooms[i][j] == 0:
          stack.append((i,j,0))
    while stack:
      i,j,val = stack.pop()
      if rooms[i][j] > val or val == 0:
        rooms[i][j] = val
        if i > 0:
          stack.append((i-1, j, val+1))
        if i < m - 1:
          stack.append((i+1, j, val+1))
        if j > 0:
          stack.append((i, j-1, val+1))
        if j < n - 1:
          stack.append((i, j+1, val+1))
        


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
