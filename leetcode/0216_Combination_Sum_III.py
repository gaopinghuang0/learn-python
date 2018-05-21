import unittest

# beats 23.28%
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # idea: backtracking
        stack = [(k, n, set(), 0)]
        res = []
        while stack:
            k, target, temp, r = stack.pop()
            if k == 1:
                if target not in temp and 1 <= target <= 9:
                    temp.add(target)
                    temp = sorted(temp)
                    if temp not in res:
                        res.append(temp)
                continue

            for i in range(r+1, 10):
                if i + k > target:
                    break
                if i not in temp:
                    temp1 = temp.copy()
                    temp1.add(i)
                    stack.append((k-1, target-i, temp1, i))
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.combinationSum3(1, 7), [[7]])
        self.assertEqual(self.s.combinationSum3(3, 7), [[1,2,4]])
        self.assertEqual(self.s.combinationSum3(3, 9), [[2,3,4],[1,3,5],[1,2,6]])
        self.assertEqual(self.s.combinationSum3(3, 3), [])
        self.assertEqual(self.s.combinationSum3(2, 3), [[1,2]])


if __name__ == "__main__":
    unittest.main()
