import unittest


# beats 77.92%, based on the same idea as 0054_Spiral_Matrix
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []

        res = [[0]*n for _ in range(n)]
        count = 1
        direct = 0
        up, left = 0, 0
        down, right = n-1, n-1
        while up <= down and left <= right:
            if direct == 0:  # move right
                for i in range(left, right+1):
                    # print(up, i)
                    res[up][i] = count
                    count += 1
                up += 1
            elif direct == 1:  # move down
                for i in range(up, down+1):
                    # print(i, right)
                    res[i][right] = count
                    count += 1
                right -= 1
            elif direct == 2:  # move left
                for i in range(right, left-1, -1):
                    # print(down, i)
                    res[down][i] = count
                    count += 1
                down -= 1
            else:  # move up
                for i in range(down, up-1, -1):
                    # print(i, left)
                    res[i][left] = count
                    count += 1
                left += 1

            direct = (direct + 1) % 4
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])
        


if __name__ == "__main__":
    unittest.main()
