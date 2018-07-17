import unittest

# beats 96.02%
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or not nums[0]:
            return nums
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        
        res = []
        row = []
        for i in range(m):
            for j in range(n):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        nums = [
         [1,2],
         [3,4]
        ]
        r = 1
        c = 4
        self.assertEqual(self.s.matrixReshape(nums, r, c), [[1,2,3,4]])
        r = 2
        c = 4
        self.assertEqual(self.s.matrixReshape(nums, r, c), nums)


if __name__ == "__main__":
    unittest.main()
