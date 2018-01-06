import unittest

# still slow, beats 10.96%
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # idea: recursion
        # do pre-check
        if target <= 0 or not candidates:
            return []
        res = []
        candidates = [num for num in candidates if num <= target]
        if sum(candidates) < target:
            return res
        for i, num in enumerate(candidates):
            if num == target:
                if [num] not in res:
                    res.append([num])
            else:
                for t_res in self.combinationSum2(candidates[:i]+candidates[i+1:], target - num):
                    t_res = [num]+t_res
                    t_res.sort()
                    if t_res not in res:
                        res.append(t_res)
        return res


# Time Limit Exceeded
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # idea: recursion
        if target <= 0 or not candidates:
            return []
        res = []
        for i, num in enumerate(candidates):
            if num > target:
                continue
            elif num == target:
                if [num] not in res:
                    res.append([num])
            else:
                for t_res in self.combinationSum2(candidates[:i]+candidates[i+1:], target - num):
                    t_res = [num]+t_res
                    t_res.sort()
                    if t_res not in res:
                        res.append(t_res)
        return res

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    print(self.s.combinationSum2([10,1,2,7,6,1,5], 8))



if __name__ == "__main__":
  unittest.main()
