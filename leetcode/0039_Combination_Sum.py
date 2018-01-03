import unittest

# speed is not too bad, beats 51.81%
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # idea: DP, recording the results from 0, 1, ..., target
        dp = {}
        dp[0] = []
        for i in range(1, target+1):
            temp = []  # list of list
            for num in candidates:
                if num > i:
                    continue
                elif num == i:
                    temp.append([num])
                else:
                    for comb in dp[i-num]:
                        comb_copy = comb[:]
                        comb_copy.append(num)
                        comb_copy.sort()
                        if comb_copy not in temp:
                            temp.append(comb_copy)
            dp[i] = temp
        return dp[target]



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.combinationSum([2, 3, 6, 7], 7), [[2,2,3], [7]])


if __name__ == "__main__":
  unittest.main()
