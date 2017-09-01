import unittest


class Solution(object):
  def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(A)
    n = len(A[0])
    nB = len(B[0])

    res = [[0 for i in range(nB)] for j in range(m)]
    for i in range(m):
      for k in range(n):
        if A[i][k]:
          for j in range(nB):
            if B[k][j]:
              res[i][j] += A[i][k] * B[k][j]
    return res



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.multiply([[1],[1]], [[1, 2]]), None)


if __name__ == "__main__":
  unittest.main()
