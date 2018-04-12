import unittest


# beats 9.82%
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # idea: use an array to store the cost from up to curr row
        if not triangle or not triangle[0]:
            return 0

        n = len(triangle)
        prev = [float('inf')] * n
        prev[0] = triangle[0][0]  # first row
        for i in range(0, n-1):  # except the last row
            curr = [float('inf')] * n
            for j in range(i+1):
                curr[j] = min(curr[j], prev[j] + triangle[i+1][j])
                curr[j+1] = min(curr[j+1], prev[j] + triangle[i+1][j+1])
            prev = curr
        # find min from curr
        return min(prev)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        triangle = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        self.assertEqual(self.s.minimumTotal(triangle), 11)
        triangle = [[-1]]
        self.assertEqual(self.s.minimumTotal(triangle), -1)


if __name__ == "__main__":
    unittest.main()
