import unittest

# idea from Discuss, beats 76.43%
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # idea from Discuss
        # reuse the idea from 0084_largest_rectange_in_histogram
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        res = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            # the following part is similar to 0084_largest_rectange_in_histogram
            stack = [-1]
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    res = max(res, h*w)
                stack.append(i)
        return res


class Solution_V1(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # idea: DP
        # DP[i][j] is the max of DP[i-1][j] and DP[i][j-1]
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[(0,0)]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    w1,h1 = dp[i-1][j]
                    w2,h2 = dp[i][j-1]
                    w, h = w2+1, h1+1
                    print(i,j, w, h)
                    if h*min(w1, w) > w*min(h,h2):
                        dp[i][j] = (min(w1, w), h)
                    else:
                        dp[i][j] = (w, min(h, h2))
                    dp[i][j] = (max(1, dp[i][j][0]), max(1, dp[i][j][1]))
                    res = max(res, dp[i][j][0]*dp[i][j][1])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        # matrix = [
        #   ["1"]
        # ]
        # self.assertEqual(self.s.maximalRectangle(matrix), 1)        
        # matrix = [
        #   ["1","0","1","0","0"],
        #   ["1","0","1","1","1"],
        #   ["1","1","1","1","1"],
        #   ["1","0","0","1","0"]
        # ]
        # self.assertEqual(self.s.maximalRectangle(matrix), 6)
        # matrix = [
        #   ["1","0","1","0","0"],
        #   ["1","1","1","1","1"],
        #   ["1","1","1","1","1"],
        #   ["1","0","0","1","0"]
        # ]
        # self.assertEqual(self.s.maximalRectangle(matrix), 10)
        # matrix = [
        #   ["1","0","1","0","0"],
        #   ["1","1","0","1","1"],
        #   ["1","1","1","1","1"],
        #   ["1","0","0","1","0"]
        # ]
        # self.assertEqual(self.s.maximalRectangle(matrix), 5)
        matrix = [
            ["1","0","1","1","1","0","0","0","1","0"],
            ["0","1","0","0","0","0","0","1","1","0"],
            ["0","1","0","1","0","0","0","0","1","1"],
            ["1","1","1","0","0","0","0","0","1","0"],
            ["0","1","1","1","0","0","1","0","1","0"],
            ["1","1","0","1","1","0","1","1","1","0"]
        ]
        self.assertEqual(self.s.maximalRectangle(matrix), 6)

if __name__ == "__main__":
    unittest.main()
