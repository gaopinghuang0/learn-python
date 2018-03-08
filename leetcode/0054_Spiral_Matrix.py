import unittest

# beats 38.89%, iterative and recursive happen to the same
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # idea 2: iterative
        if not matrix or not matrix[0]:
            return []
        res = []
        up, left = 0, 0
        down, right = len(matrix) - 1, len(matrix[0]) - 1
        direct = 0
        while up <= down and left <= right:
            if direct == 0:  # move right
                for j in range(left, right+1):
                    res.append(matrix[up][j])
                up += 1
            elif direct == 1:  ## move down
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif direct == 2:  # move left
                for j in range(right, left-1, -1):
                    res.append(matrix[down][j])
                down -= 1
            else:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            direct = (direct+1) % 4
        return res


# beats 38.89%
class SolutionFastRecursion(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # idea: recursive, go the outer border, then call inner matrix
        if not matrix or not matrix[0]:
            return []

        def go_spiral(matrix, x, y, m, n):
            if x > m or y > n:
                return []
            res = []
            for j in range(y, n+1):
                res.append(matrix[x][j])
            # print(res)
            for i in range(x+1, m+1):
                res.append(matrix[i][n])
            # print(res)
            if m > x:
                for j in range(n-1, y-1, -1):
                    res.append(matrix[m][j])
            # print(res)
            if n > y:
                for i in range(m-1, x, -1):
                    res.append(matrix[i][y])
            # print(res)
            res += go_spiral(matrix, x+1, y+1, m-1, n-1)
            return res

        return go_spiral(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1)



# beats 2.54%
class SolutionSlowRecursive(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # idea: recursive, go the outer border, then call inner matrix
        if not matrix or not matrix[0]:
            return []

        def go_spiral(matrix, x, y, m, n):
            if m <= 0 or n <= 0:
                return []
            res = []
            for j in range(y, y+n):
                res.append(matrix[x][j])
            # print(res)
            for i in range(x+1, x+m):
                res.append(matrix[i][y+n-1])
            # print(res)
            if m >= 2:
                for j in range(y+n-2, y-1, -1):
                    res.append(matrix[x+m-1][j])
            # print(res)
            if n >= 2:
                for i in range(x+m-2, x, -1):
                    res.append(matrix[i][y])
            # print(res)
            res += go_spiral(matrix, x+1, y+1, m-2, n-2)
            return res

        return go_spiral(matrix, 0, 0, len(matrix), len(matrix[0]))



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    print(self.s.spiralOrder(matrix))
    matrix = [[2,3]]
    print(self.s.spiralOrder(matrix))
    matrix = [[1,2],[3,4]]
    print(self.s.spiralOrder(matrix))


if __name__ == "__main__":
  unittest.main()
