import unittest


# beats 44.34%
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea: DP
        square_nums = []
        i = 1
        while i*i <= n:
            square_nums.append(i*i)
            i += 1

        dp = {}
        for i in range(1, n+1):
            least = i   # least number is 1+1+...+1 (total i items)
            for num in square_nums:
                if i == num:
                    dp[i] = 1
                    least = 1
                    break
                elif i > num:
                    tmp = 1 + dp[i - num]
                    least = min(least, tmp)
                else:   # i < num
                    break
            dp[i] = least
        return dp[n]

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
