import unittest


class Solution(object):
  def findMedianSortedArrays(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: float
    """
    # Credit: https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
    m, n = len(A), len(B)
    if m > n:   # workon m <= n
      m, n, A, B = n, m, B, A
    if n == 0:
      raise ValueError

    # binary search on [0,m]
    i_left, i_right, half_len = 0, m, (m+n+1)//2
    while i_left <= i_right:
      i = (i_left + i_right) // 2
      j = half_len - i
      if i < m and A[i] < B[j-1]:
        # i is too small, increase i
        i_left = i + 1
      elif i > 0 and A[i-1] > B[j]:
        # i is too big, decrease
        i_right = i - 1
      else:
        if i == 0:
          max_left = B[j-1]
        elif j == 0:
          max_left = A[i-1]
        else:
          max_left = max(A[i-1], B[j-1])

        if (m+n) % 2 == 1:
          return max_left

        if i == m:
          min_right = B[j]
        elif j == n:
          min_right = A[i]
        else:
          min_right = min(A[i], B[j])

        return (max_left + min_right) / 2



# [], [] -> Error
# [1,3], [2]  -> 2.0
# [1,2], [3,4] -> 2.5


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.findMedianSortedArrays([1,3], [2]), 2.0)
    self.assertEqual(self.s.findMedianSortedArrays([1,2], [3,4]), 2.5)


if __name__ == "__main__":
  unittest.main()
